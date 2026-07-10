"""Root agent implementation."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from agents.agent import Agent
from agents.agent_result import AgentResult
from context.execution_event import ExecutionEvent
from registry.agent_registry import AgentRegistry

if TYPE_CHECKING:
    from context.request_context import RequestContext


class RootAgent(Agent):
    """The entry point agent responsible for orchestrating the research workflow."""

    def __init__(self, agent_registry: AgentRegistry) -> None:
        """Initializes the root agent with the agent registry.

        Args:
            agent_registry: Registry containing all available agents.
        """
        self._agent_registry = agent_registry

    def name(self) -> str:
        """Gets the name of the agent."""
        return "root"

    def description(self) -> str:
        """Gets a brief description of the agent."""
        return "The orchestrating root agent."

    def execute(self, context: "RequestContext") -> AgentResult:
        """Executes the research workflow via a downstream agent."""
        # Retrieve and execute research agent
        research_agent = self._agent_registry.get("mock_research_agent")
        result = research_agent.execute(context)

        # Append execution event
        event = ExecutionEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            component=self.name(),
            component_type="agent",
            event_type="completed",
            details={"executed_agent": research_agent.name()},
            duration_ms=0.0,
        )
        context.execution_trace.append(event)

        return result
