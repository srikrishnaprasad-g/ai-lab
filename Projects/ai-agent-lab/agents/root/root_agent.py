"""Root agent implementation."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from agents.agent import Agent
from agents.agent_result import AgentResult
from context.execution_event import ExecutionEvent
from registry.agent_registry import AgentRegistry
from registry.tool_registry import ToolRegistry

if TYPE_CHECKING:
    from context.request_context import RequestContext


class RootAgent(Agent):
    """The entry point agent responsible for orchestrating the research workflow."""

    def __init__(self, agent_registry: AgentRegistry, tool_registry: ToolRegistry) -> None:
        """Initializes the root agent with agent and tool registries.

        Args:
            agent_registry: Registry containing all available agents.
            tool_registry: Registry containing all available tools.
        """
        self._agent_registry = agent_registry
        self._tool_registry = tool_registry

    def name(self) -> str:
        """Gets the name of the agent."""
        return "root"

    def description(self) -> str:
        """Gets a brief description of the agent."""
        return "The orchestrating root agent."

    def execute(self, context: "RequestContext") -> AgentResult:
        """Executes the research workflow via downstream agents and tools."""
        # Execute workflow components
        self._agent_registry.get("mock_research_agent").execute(context)
        self._agent_registry.get("mock_summary_agent").execute(context)
        self._tool_registry.get("mock_pdf_tool").execute(context)

        # Append execution event
        event = ExecutionEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            component=self.name(),
            component_type="agent",
            event_type="completed",
            details={"workflow": "research_summary_pdf"},
            duration_ms=0.0,
        )
        context.execution_trace.append(event)

        return AgentResult(
            success=True,
            output="Workflow completed successfully.",
            metadata={"agent": self.name(), "source": "root"}
        )
