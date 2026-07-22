"""Search Service implementation."""

from search.search_provider import SearchProvider
from search.search_response import SearchResponse

class SearchService:
    """Reusable service that wraps a SearchProvider."""
    
    def __init__(self, provider: SearchProvider) -> None:
        self._provider = provider

    def perform_search(self, query: str, max_results: int | None = None) -> SearchResponse:
        """Performs a search using the injected provider."""
        return self._provider.search(query, max_results)
