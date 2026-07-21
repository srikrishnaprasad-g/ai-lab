"""Factory for production agents."""

from agents.research_agent import ResearchAgent
from observability.telemetry_service import TelemetryService

class AgentFactory:
    """Factory for creating production-ready agents."""

    def __init__(self, telemetry_service: TelemetryService) -> None:
        """Initializes the agent factory.

        Args:
            telemetry_service: Telemetry service to inject into agents.
        """
        self._telemetry_service = telemetry_service

    def create_research_agent(self) -> ResearchAgent:
        """Creates a new ResearchAgent.

        Returns:
            An instantiated ResearchAgent.
        """
        return ResearchAgent(self._telemetry_service)
