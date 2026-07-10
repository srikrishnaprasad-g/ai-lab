"""Mock research agent implementation."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from agents.agent import Agent
from agents.agent_result import AgentResult
from context.execution_event import ExecutionEvent
from registry.tool_registry import ToolRegistry

if TYPE_CHECKING:
    from context.request_context import RequestContext


class MockResearchAgent(Agent):
    """A deterministic mock implementation of a research agent."""

    def __init__(self, tool_registry: ToolRegistry) -> None:
        """Initializes the agent with required tool registry.

        Args:
            tool_registry: Registry containing tools to be used by the agent.
        """
        self._tool_registry = tool_registry

    def name(self) -> str:
        """Gets the name of the agent."""
        return "mock_research_agent"

    def description(self) -> str:
        """Gets a brief description of the agent."""
        return "A mock research agent that uses a search tool."

    def execute(self, context: "RequestContext") -> AgentResult:
        """Executes the mock research process."""
        # Retrieve and execute tool
        search_tool = self._tool_registry.get("mock_web_search")
        search_tool.execute(context)

        # Read results and build summary
        search_results = context.working_memory.get("search_results", [])
        summary = "Research results:\n" + "\n".join([f"- {r['title']}" for r in search_results])

        # Store summary in memory
        context.working_memory["research_summary"] = summary

        # Append execution event
        event = ExecutionEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            component=self.name(),
            component_type="agent",
            event_type="completed",
            details={"summary_length": len(summary)},
            duration_ms=0.0
        )
        context.execution_trace.append(event)

        return AgentResult(
            success=True,
            output=summary,
            metadata={
                "agent": self.name(),
                "source": "mock",
                "documents": len(search_results)
            }
        )
