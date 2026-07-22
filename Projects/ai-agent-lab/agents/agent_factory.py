"""Factory for production agents."""

from agents.research_agent import ResearchAgent
from search.search_service import SearchService
from observability.telemetry_service import TelemetryService

class AgentFactory:
    """Factory for creating production-ready agents."""

    def __init__(self, telemetry_service: TelemetryService, search_service: SearchService) -> None:
        """Initializes the agent factory.

        Args:
            telemetry_service: Telemetry service to inject into agents.
            search_service: Search service to inject into agents.
        """
        self._telemetry_service = telemetry_service
        self._search_service = search_service

    def create_research_agent(self) -> ResearchAgent:
        """Creates a new ResearchAgent.

        Returns:
            An instantiated ResearchAgent.
        """
        return ResearchAgent(self._telemetry_service, self._search_service)
