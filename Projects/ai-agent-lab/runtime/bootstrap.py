"""Runtime bootstrap for assembling components."""

from registry.agent_registry import AgentRegistry
from registry.tool_registry import ToolRegistry
from tools.mock.mock_web_search_tool import MockWebSearchTool
from agents.mock.mock_research_agent import MockResearchAgent
from agents.root.root_agent import RootAgent
from runtime.orchestrator import RuntimeOrchestrator


class RuntimeBootstrap:
    """Responsible for assembling the runtime components."""

    @staticmethod
    def build_runtime() -> RuntimeOrchestrator:
        """Assembles and wires together the runtime components.

        Returns:
            An instantiated RuntimeOrchestrator.
        """
        # Create registries
        tool_registry = ToolRegistry()
        agent_registry = AgentRegistry()

        # Register tools
        tool_registry.register(MockWebSearchTool())

        # Create and register agents
        research_agent = MockResearchAgent(tool_registry=tool_registry)
        agent_registry.register(research_agent)

        root_agent = RootAgent(agent_registry=agent_registry)
        agent_registry.register(root_agent)

        # Create orchestrator
        orchestrator = RuntimeOrchestrator(
            agent_registry=agent_registry,
            tool_registry=tool_registry,
            root_agent=root_agent.name(),
        )

        return orchestrator
