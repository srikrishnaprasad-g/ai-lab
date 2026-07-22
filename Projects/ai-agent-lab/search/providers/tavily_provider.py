"""Tavily search provider implementation."""

from typing import Any
from search.exceptions import SearchException, SearchProviderError
from search.http_exceptions import HTTPRequestError
from search.search_provider import SearchProvider
from search.search_response import SearchResponse
from search.search_result import SearchResult
from search.http_client import HttpClient
from search.search_provider_config import SearchProviderConfig


class TavilyProvider(SearchProvider):
    """Production implementation of Tavily search."""

    def __init__(self, http_client: HttpClient, config: SearchProviderConfig, api_key: str) -> None:
        self._http_client = http_client
        self._config = config
        self._api_key = api_key
        self._api_url = "https://api.tavily.com/search"

    def provider_name(self) -> str:
        """Returns the name of the provider."""
        return "tavily"

    def search(self, query: str, max_results: int | None = None) -> SearchResponse:
        """Executes search query against Tavily API."""
        if not query.strip():
            raise SearchException("Query cannot be empty.")
        
        limit = max_results or self._config.max_results
        
        try:
            # Tavily API expects POST request
            payload = {
                "api_key": self._api_key,
                "query": query,
                "max_results": limit,
                "search_depth": "basic",
            }
            data = self._http_client.post(self._api_url, json=payload)
            
            # Map Tavily response structure to SearchResponse
            results = []
            if "results" in data:
                for i, res in enumerate(data["results"][:limit]):
                    results.append(SearchResult(
                        title=res.get("title", ""),
                        url=res.get("url", ""),
                        snippet=res.get("content", ""),
                        rank=i + 1,
                        metadata={"raw": res}
                    ))
            
            return SearchResponse(
                results=results,
                provider=self.provider_name(),
                query=query,
                metadata={
                    "provider": self.provider_name(),
                },
            )
        except HTTPRequestError as e:
            # Handle invalid API key (401) specifically
            if e.status_code == 401:
                raise SearchProviderError("Invalid Tavily API key.") from e
            raise SearchProviderError(f"Provider request error: {e}") from e
        except Exception as e:
            raise SearchProviderError(f"Unexpected provider error: {e}") from e
