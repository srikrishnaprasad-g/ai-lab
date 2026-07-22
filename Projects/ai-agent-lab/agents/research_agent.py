"""Production research agent implementation."""

import time
from search.search_service import SearchService
from search.exceptions import SearchProviderError
from context.request_context import RequestContext
from agents.agent_result import AgentResult
from agents.base_agent import BaseAgent
from agents.agent_capabilities import AgentCapabilities
from observability.telemetry_service import TelemetryService
from agents.research.research_result import ResearchResult

class ResearchAgent(BaseAgent):
    """Production research agent."""

    def __init__(self, telemetry_service: TelemetryService, search_service: SearchService) -> None:
        """Initializes the research agent."""
        self._search_service = search_service
        capabilities = AgentCapabilities(
            supported_actions=["research"],
            supported_tools=["web_search"],
            execution_requirements=["web_search_tool"]
        )
        super().__init__(
            name="research_agent",
            description="Performs research using available tools.",
            telemetry_service=telemetry_service,
            capabilities=capabilities
        )

    def _execute(self, context: RequestContext) -> AgentResult:
        """Executes research logic."""
        if not context.user_request.strip():
            return AgentResult(success=False, output=None, errors=["Empty query."])
            
        start_time = time.perf_counter()
        
        try:
            search_response = self._search_service.perform_search(context.user_request)
        except SearchProviderError as e:
            return AgentResult(success=False, output=None, errors=[str(e)])
        except Exception as e:
            return AgentResult(success=False, output=None, errors=[f"Unexpected provider error: {e}"])
        
        duration = time.perf_counter() - start_time
        
        research_result = ResearchResult(
            original_query=context.user_request,
            search_provider=search_response.provider,
            source_count=len(search_response.results),
            sources=search_response.results,
            observations=[r.snippet for r in search_response.results],
            processing_duration=duration,
            raw_search_response=search_response
        )
        
        return AgentResult(success=True, output=research_result)
