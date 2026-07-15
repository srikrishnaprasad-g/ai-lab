"""Mock DuckDuckGo provider implementation."""

from search.exceptions import SearchException, SearchTimeoutError, SearchProviderError
from search.http_exceptions import HTTPTimeoutError, HTTPRequestError
from search.search_provider import SearchProvider
from search.search_response import SearchResponse
from search.search_result import SearchResult
from search.http_client import HttpClient
from search.search_provider_config import SearchProviderConfig


class DuckDuckGoProvider(SearchProvider):
    """Deterministic mock implementation of DuckDuckGo search."""

    def __init__(self, http_client: HttpClient, config: SearchProviderConfig) -> None:
        self._http_client = http_client
        self._config = config

    def provider_name(self) -> str:
        """Returns the name of the provider."""
        return "duckduckgo"

    def search(self, query: str, max_results: int | None = None) -> SearchResponse:
        """Returns deterministic mock search results."""
        if not query.strip():
            raise SearchException("Query cannot be empty.")
        
        limit = max_results or self._config.max_results
        if limit <= 0:
            raise SearchException("max_results must be greater than zero.")
        
        # Example of how to use HttpClient safely with exception mapping
        # try:
        #     self._http_client.get("...")
        # except HTTPTimeoutError as e:
        #     raise SearchTimeoutError(f"Provider timed out: {e}") from e
        # except HTTPRequestError as e:
        #     raise SearchProviderError(f"Provider request error: {e}") from e

        results = [
            SearchResult(
                title=f"Mock Result {i+1} for {query}",
                url=f"https://duckduckgo.com/r{i+1}",
                snippet=f"This is mock snippet {i+1}.",
                rank=i + 1,
            )
            for i in range(min(limit, 3))
        ]
        return SearchResponse(
            results=results,
            provider=self.provider_name(),
            query=query,
            metadata={
                "provider": self.provider_name(),
                "max_results": limit,
            },
        )
