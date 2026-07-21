"""Unit tests for the Tool Framework."""
from tools.search.web_search_tool import WebSearchTool
from search.providers.mock_search_provider import MockSearchProvider
from context.request_context import RequestContext
from tools.tool_result import ToolResult

def test_web_search_tool_execution():
    print("Testing WebSearchTool execution...")
    provider = MockSearchProvider()
    tool = WebSearchTool(search_provider=provider, max_results=1)
    
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test query")
    result = tool.execute(context)
    
    assert isinstance(result, ToolResult)
    assert result.success is True
    assert result.output == 1
    assert "web_search" in result.metadata["tool"]
    print("WebSearchTool execution PASSED.")

def test_tool_registry_placeholder():
    # Registry test is indirect via Orchestrator, but we can verify registration 
    # logic if we expose the registry here. 
    # For now, verify WebSearchTool interface adherence.
    print("Testing WebSearchTool interface...")
    assert hasattr(WebSearchTool, "name")
    assert hasattr(WebSearchTool, "description")
    print("WebSearchTool interface PASSED.")

if __name__ == "__main__":
    test_web_search_tool_execution()
    test_tool_registry_placeholder()
    print("All tool framework tests PASSED.")
