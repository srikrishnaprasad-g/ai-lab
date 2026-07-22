"""Factory for production agents."""

from agents.research_agent import ResearchAgent
from agents.summary.summary_agent import SummaryAgent
from prompts.prompt_registry import PromptRegistry
from prompts.summary_prompt_builder import SummaryPromptBuilder
from search.search_service import SearchService
from observability.telemetry_service import TelemetryService

class AgentFactory:
    """Factory for creating production-ready agents."""

    def __init__(self, telemetry_service: TelemetryService, search_service: SearchService, prompt_registry: PromptRegistry) -> None:
        """Initializes the agent factory.

        Args:
            telemetry_service: Telemetry service to inject into agents.
            search_service: Search service to inject into agents.
            prompt_registry: Prompt registry for builders.
        """
        self._telemetry_service = telemetry_service
        self._search_service = search_service
        self._prompt_registry = prompt_registry

    def create_research_agent(self) -> ResearchAgent:
        """Creates a new ResearchAgent.

        Returns:
            An instantiated ResearchAgent.
        """
        return ResearchAgent(self._telemetry_service, self._search_service)
        
    def create_summary_agent(self) -> SummaryAgent:
        """Creates a new SummaryAgent.

        Returns:
            An instantiated SummaryAgent.
        """
        prompt_builder = SummaryPromptBuilder(self._prompt_registry)
        return SummaryAgent(self._telemetry_service, prompt_builder)
