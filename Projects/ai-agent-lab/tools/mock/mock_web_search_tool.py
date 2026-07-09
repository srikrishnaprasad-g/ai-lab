"""Mock web search tool implementation."""

import uuid
from datetime import datetime, timezone
from typing import Any

from tools.tool import Tool
from tools.tool_result import ToolResult
from context.request_context import RequestContext
from context.execution_event import ExecutionEvent


class MockWebSearchTool(Tool):
    """A deterministic mock implementation of a web search tool."""

    def name(self) -> str:
        """Gets the name of the tool."""
        return "mock_web_search"

    def description(self) -> str:
        """Gets a brief description of the tool's purpose."""
        return "Performs a deterministic mock web search."

    def execute(self, context: "RequestContext") -> ToolResult:
        """Executes the mock web search and updates the context."""
        # Hardcoded search results
        search_results = [
            {"title": "Result 1", "url": "https://example.com/1", "snippet": "Snippet 1"},
            {"title": "Result 2", "url": "https://example.com/2", "snippet": "Snippet 2"},
            {"title": "Result 3", "url": "https://example.com/3", "snippet": "Snippet 3"},
        ]

        # Update working memory
        context.working_memory["search_results"] = search_results

        # Append execution event
        event = ExecutionEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            component=self.name(),
            component_type="tool",
            event_type="completed",
            details={"query": context.user_request, "result_count": len(search_results)},
            duration_ms=0.0
        )
        context.execution_trace.append(event)

        return ToolResult(
            success=True,
            output=search_results,
            metadata={
                "tool": self.name(),
                "source": "mock",
                "documents": search_results
            },
        )
