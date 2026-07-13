"""Web search tool implementation."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from tools.tool import Tool
from tools.tool_result import ToolResult
from context.execution_event import ExecutionEvent
from context import keys
from search.search_provider import SearchProvider

if TYPE_CHECKING:
    from context.request_context import RequestContext


class WebSearchTool(Tool):
    """Production-quality web search tool utilizing SearchProvider."""

    def __init__(self, search_provider: SearchProvider, max_results: int) -> None:
        """Initializes the tool with a search provider and max_results.

        Args:
            search_provider: The search provider to use.
            max_results: The maximum number of results to retrieve.
        """
        self._search_provider = search_provider
        self._max_results = max_results

    def name(self) -> str:
        """Gets the name of the tool."""
        return "web_search"

    def description(self) -> str:
        """Gets a brief description of the tool."""
        return "Performs web searches using the configured search provider."

    def execute(self, context: "RequestContext") -> ToolResult:
        """Executes search and updates the context with SearchResponse."""
        # Execute search
        search_response = self._search_provider.search(context.user_request, self._max_results)

        # Update working memory with complete response
        context.working_memory[keys.SEARCH_RESPONSE] = search_response

        # Append execution event
        event = ExecutionEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            component=self.name(),
            component_type="tool",
            event_type="completed",
            details={
                "provider": search_response.provider,
                "result_count": len(search_response.results)
            },
            duration_ms=0.0,
        )
        context.execution_trace.append(event)

        return ToolResult(
            success=True,
            output=len(search_response.results),
            metadata={
                "tool": self.name(),
                "provider": search_response.provider,
            },
        )
