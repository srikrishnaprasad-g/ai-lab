"""Mock summary agent implementation."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from agents.agent import Agent
from agents.agent_result import AgentResult
from context.execution_event import ExecutionEvent
from context import keys

if TYPE_CHECKING:
    from context.request_context import RequestContext


class MockSummaryAgent(Agent):
    """A deterministic mock implementation of a summary agent."""

    def name(self) -> str:
        """Gets the name of the agent."""
        return "mock_summary_agent"

    def description(self) -> str:
        """Gets a brief description of the agent."""
        return "A mock summary agent that processes search results."

    def execute(self, context: "RequestContext") -> AgentResult:
        """Executes the mock summarization process."""
        # Read search results
        search_response = context.working_memory.get(keys.SEARCH_RESPONSE)
        search_results = search_response.results if search_response else []
        
        # Build summary
        summary = f"Summarized {len(search_results)} search results into a final report."

        # Store summary in memory
        context.working_memory[keys.FINAL_SUMMARY] = summary

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
