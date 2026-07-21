"""Mock search provider for testing."""
from search.search_provider import SearchProvider
from search.search_response import SearchResponse
from search.search_result import SearchResult

class MockSearchProvider(SearchProvider):
    """Deterministic mock search provider."""
    
    def search(self, query: str, max_results: int | None = None) -> SearchResponse:
        """Returns dummy search results."""
        results = [
            SearchResult(title="Result 1", url="http://test.com/1", snippet="Snippet 1", rank=1),
            SearchResult(title="Result 2", url="http://test.com/2", snippet="Snippet 2", rank=2),
        ]
        if max_results:
            results = results[:max_results]
            
        return SearchResponse(
            results=results,
            provider="mock_provider",
            query=query
        )
        
    def provider_name(self) -> str:
        """Returns the name of the mock provider."""
        return "mock_provider"
