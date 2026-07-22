"""Unit tests for the Search Framework."""
from typing import Any
from search.providers.tavily_provider import TavilyProvider
from search.search_provider_config import SearchProviderConfig
from search.http_client import HttpClient
from unittest.mock import MagicMock

# Mock HttpClient
class MockHttpClient(HttpClient):
    def __init__(self) -> None:
        pass # Don't initialize httpx.Client
        
    def post(self, url: str, json: dict[str, Any] | None = None) -> Any:
        return {"results": [{"content": "Result 1", "title": "http://r1"}]}

def test_tavily_provider_search():
    print("Testing TavilyProvider search...")
    mock_client = MockHttpClient()
    config = SearchProviderConfig(max_results=5)
    provider = TavilyProvider(mock_client, config, api_key="test_key")
    
    response = provider.search("test query")
    assert response.provider == "tavily"
    assert len(response.results) == 1
    assert response.results[0].snippet == "Result 1"
    print("TavilyProvider search PASSED.")

def test_tavily_provider_error():
    print("Testing TavilyProvider error handling...")
    mock_client = MagicMock(spec=HttpClient)
    # The provider wraps HTTPRequestError in SearchProviderError
    mock_client.post.side_effect = Exception("HTTP Error")
    
    config = SearchProviderConfig(max_results=5)
    provider = TavilyProvider(mock_client, config, api_key="test_key")
    
    try:
        provider.search("test query")
        assert False, "Should have raised SearchProviderError"
    except Exception:
        pass
    print("TavilyProvider error handling PASSED.")

if __name__ == "__main__":
    test_tavily_provider_search()
    test_tavily_provider_error()
    print("All search framework tests PASSED.")
