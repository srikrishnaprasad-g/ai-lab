"""Runtime bootstrap implementation."""

from runtime.runtime_orchestrator import RuntimeOrchestrator
from runtime.planner.planner import TaskPlanner
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from runtime.pipeline.telemetry_stage import TelemetryStage
from runtime.pipeline.retry_stage import RetryStage
from observability.telemetry_service import TelemetryService
from registry.agent_registry import AgentRegistry
from registry.tool_registry import ToolRegistry
from agents.agent_factory import AgentFactory
from tools.search.web_search_tool import WebSearchTool
from search.providers.mock_search_provider import MockSearchProvider
from prompts.prompt_registry import PromptRegistry
from prompts.prompt_builder import DefaultPromptBuilder
from prompts.templates import RESEARCH_TEMPLATE, SUMMARIZATION_TEMPLATE, WRITING_TEMPLATE
from llm.providers.mock_llm_provider import MockLLMProvider


class RuntimeBootstrap:
    """Composition root for the runtime components."""

    @staticmethod
    def build() -> RuntimeOrchestrator:
        """Constructs and wires the runtime components.

        Returns:
            A fully configured RuntimeOrchestrator instance.
        """
        # 1. Telemetry
        telemetry_service = TelemetryService()
        
        # 2. Pipeline Stages
        telemetry_stage = TelemetryStage(telemetry_service)
        retry_stage = RetryStage(max_attempts=3, retry_exceptions=(Exception,))
        
        # 3. Pipeline
        pipeline = ExecutionPipeline([telemetry_stage, retry_stage])
        
        # 4. Planner
        planner = TaskPlanner()
        
        # 5. Prompt Framework
        prompt_registry = PromptRegistry()
        prompt_registry.register(RESEARCH_TEMPLATE)
        prompt_registry.register(SUMMARIZATION_TEMPLATE)
        prompt_registry.register(WRITING_TEMPLATE)
        prompt_builder = DefaultPromptBuilder(prompt_registry)
        
        # 6. LLM Provider
        llm_provider = MockLLMProvider()
        
        # 7. Tool Framework
        tool_registry = ToolRegistry()
        search_provider = MockSearchProvider()
        web_search_tool = WebSearchTool(search_provider, max_results=5)
        tool_registry.register(web_search_tool)
        
        # 8. Agent Framework
        agent_registry = AgentRegistry()
        agent_factory = AgentFactory(telemetry_service, tool_registry, prompt_builder, llm_provider)
        
        research_agent = agent_factory.create_research_agent()
        agent_registry.register(research_agent)
        
        # 9. Orchestrator
        orchestrator = RuntimeOrchestrator(planner, pipeline, agent_registry)
        
        return orchestrator
