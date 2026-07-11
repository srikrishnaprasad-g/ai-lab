"""Mock DuckDuckGo provider implementation."""

from search.exceptions import SearchException
from search.search_provider import SearchProvider
from search.search_response import SearchResponse
from search.search_result import SearchResult


class DuckDuckGoProvider(SearchProvider):
    """Deterministic mock implementation of DuckDuckGo search."""

    def provider_name(self) -> str:
        """Returns the name of the provider."""
        return "duckduckgo"

    def search(self, query: str, max_results: int) -> SearchResponse:
        """Returns deterministic mock search results."""
        if not query.strip():
            raise SearchException("Query cannot be empty.")
        if max_results <= 0:
            raise SearchException("max_results must be greater than zero.")

        results = [
            SearchResult(
                title=f"Mock Result {i+1} for {query}",
                url=f"https://duckduckgo.com/r{i+1}",
                snippet=f"This is mock snippet {i+1}.",
                rank=i + 1,
            )
            for i in range(min(max_results, 3))
        ]
        return SearchResponse(
            results=results,
            provider=self.provider_name(),
            query=query,
            metadata={
                "provider": self.provider_name(),
                "max_results": max_results,
            },
        )
