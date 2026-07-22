"""Unit tests for ResearchAgent."""
from unittest.mock import MagicMock
from agents.research_agent import ResearchAgent
from search.search_service import SearchService
from search.search_response import SearchResponse
from search.search_result import SearchResult
from observability.telemetry_service import TelemetryService
from context.request_context import RequestContext
from agents.research.research_result import ResearchResult

def test_research_agent_successful_search():
    print("Testing ResearchAgent successful search...")
    # Mock services
    telemetry = MagicMock(spec=TelemetryService)
    search_service = MagicMock(spec=SearchService)
    
    # Mock successful response
    mock_results = [SearchResult(title="Result 1", url="http://r1", snippet="Snippet 1", rank=1)]
    search_response = SearchResponse(results=mock_results, provider="mock", query="test")
    search_service.perform_search.return_value = search_response
    
    agent = ResearchAgent(telemetry, search_service)
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test query")
    
    result = agent.execute(context)
    
    assert result.success is True
    assert isinstance(result.output, ResearchResult)
    assert result.output.source_count == 1
    assert result.output.sources[0].title == "Result 1"
    assert "Snippet 1" in result.output.observations[0]
    print("ResearchAgent successful search PASSED.")

def test_research_agent_empty_query():
    print("Testing ResearchAgent empty query...")
    telemetry = MagicMock(spec=TelemetryService)
    search_service = MagicMock(spec=SearchService)
    
    agent = ResearchAgent(telemetry, search_service)
    context = RequestContext(request_id="1", correlation_id="c1", user_request="  ")
    
    result = agent.execute(context)
    assert result.success is False
    assert len(result.errors) > 0
    assert "Empty query" in result.errors[0]
    print("ResearchAgent empty query PASSED.")

def test_research_agent_no_results():
    print("Testing ResearchAgent no results...")
    telemetry = MagicMock(spec=TelemetryService)
    search_service = MagicMock(spec=SearchService)
    
    # Mock empty response
    search_response = SearchResponse(results=[], provider="mock", query="test")
    search_service.perform_search.return_value = search_response
    
    agent = ResearchAgent(telemetry, search_service)
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test query")
    
    result = agent.execute(context)
    
    assert result.success is True
    assert isinstance(result.output, ResearchResult)
    assert result.output.source_count == 0
    print("ResearchAgent no results PASSED.")

if __name__ == "__main__":
    test_research_agent_successful_search()
    test_research_agent_empty_query()
    test_research_agent_no_results()
    print("All research agent tests PASSED.")
