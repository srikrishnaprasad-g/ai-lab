"""Runtime bootstrap implementation."""

from runtime.orchestrator.orchestrator import RuntimeOrchestrator
from runtime.planner.planner import TaskPlanner
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from runtime.pipeline.telemetry_stage import TelemetryStage
from runtime.pipeline.retry_stage import RetryStage
from observability.telemetry_service import TelemetryService
from registry.agent_registry import AgentRegistry
from agents.agent_factory import AgentFactory
from search.search_service import SearchService
from search.search_provider_factory import SearchProviderFactory
from llm.llm_provider_factory import LLMProviderFactory
from prompts.prompt_registry import PromptRegistry
from agents.pdf.reportlab_generator import ReportLabGenerator
from config.settings import load_settings


class RuntimeBootstrap:
    """Composition root for the runtime components."""

    @staticmethod
    def build() -> RuntimeOrchestrator:
        """Constructs and wires the runtime components.

        Returns:
            A fully configured RuntimeOrchestrator instance.
        """
        # 1. Settings
        settings = load_settings()
        
        # 2. Telemetry
        telemetry_service = TelemetryService()
        
        # 3. Pipeline Stages
        telemetry_stage = TelemetryStage(telemetry_service)
        retry_stage = RetryStage(max_attempts=3, retry_exceptions=(Exception,))
        
        # 4. Pipeline
        pipeline = ExecutionPipeline([telemetry_stage, retry_stage])
        
        # 5. Planner
        planner = TaskPlanner()
        
        # 6. Search Framework
        provider_factory = SearchProviderFactory(settings)
        search_provider = provider_factory.create_provider()
        search_service = SearchService(search_provider)
        
        # 7. LLM Framework
        llm_factory = LLMProviderFactory(settings)
        llm_provider = llm_factory.create_provider()
        
        # 8. Prompt Framework
        prompt_registry = PromptRegistry()
        
        # 9. PDF Framework
        pdf_generator = ReportLabGenerator()
        
        # 10. Agent Framework
        agent_registry = AgentRegistry()
        agent_factory = AgentFactory(telemetry_service, search_service, prompt_registry, pdf_generator, llm_provider)
        
        research_agent = agent_factory.create_research_agent()
        agent_registry.register(research_agent)
        
        summary_agent = agent_factory.create_summary_agent()
        agent_registry.register(summary_agent)
        
        pdf_agent = agent_factory.create_pdf_agent()
        agent_registry.register(pdf_agent)
        
        # 11. Orchestrator
        orchestrator = RuntimeOrchestrator(planner, pipeline, agent_registry)
        
        return orchestrator
