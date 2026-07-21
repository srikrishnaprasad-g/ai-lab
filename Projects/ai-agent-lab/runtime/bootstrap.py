"""Runtime bootstrap for assembling components."""

from config.settings import load_settings
from registry.agent_registry import AgentRegistry
from registry.tool_registry import ToolRegistry
from search.search_provider_factory import SearchProviderFactory
from tools.search.web_search_tool import WebSearchTool
from tools.pdf.mock_pdf_tool import MockPDFTool
from agents.mock.mock_research_agent import MockResearchAgent
from agents.summary.mock_summary_agent import MockSummaryAgent
from agents.root.root_agent import RootAgent
from runtime.orchestrator import RuntimeOrchestrator
from llm.llm_provider_factory import LLMProviderFactory
from prompts.summary_prompt_builder import SummaryPromptBuilder
from observability.telemetry_service import TelemetryService


class RuntimeBootstrap:
    """Responsible for assembling the runtime components."""

    @staticmethod
    def build_runtime() -> RuntimeOrchestrator:
        """Assembles and wires together the runtime components.

        Returns:
            An instantiated RuntimeOrchestrator.
        """
        # Load settings and create factory
        settings = load_settings()
        search_provider_factory = SearchProviderFactory(settings)
        search_provider = search_provider_factory.create_provider()
        
        llm_provider_factory = LLMProviderFactory(settings)
        llm_provider = llm_provider_factory.create_provider()
        
        prompt_builder = SummaryPromptBuilder()
        
        telemetry_service = TelemetryService()

        # Create registries
        tool_registry = ToolRegistry()
        agent_registry = AgentRegistry()

        # Register tools
        tool_registry.register(
            WebSearchTool(
                search_provider=search_provider,
                max_results=settings.default_search_max_results,
            )
        )
        tool_registry.register(MockPDFTool())

        # Create and register agents
        research_agent = MockResearchAgent(tool_registry=tool_registry)
        agent_registry.register(research_agent)

        summary_agent = MockSummaryAgent(
            llm_provider=llm_provider, 
            default_model=settings.default_llm_model,
            prompt_builder=prompt_builder
        )
        agent_registry.register(summary_agent)

        root_agent = RootAgent(agent_registry=agent_registry, tool_registry=tool_registry)
        agent_registry.register(root_agent)

        # Create orchestrator
        orchestrator = RuntimeOrchestrator(
            agent_registry=agent_registry,
            tool_registry=tool_registry,
            telemetry_service=telemetry_service,
            root_agent=root_agent.name(),
        )

        return orchestrator
