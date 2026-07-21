"""Factory for production agents."""

from agents.research_agent import ResearchAgent
from registry.tool_registry import ToolRegistry
from prompts.prompt_builder import PromptBuilder
from llm.llm_provider import LLMProvider
from observability.telemetry_service import TelemetryService

class AgentFactory:
    """Factory for creating production-ready agents."""

    def __init__(self, telemetry_service: TelemetryService, tool_registry: ToolRegistry, prompt_builder: PromptBuilder, llm_provider: LLMProvider) -> None:
        """Initializes the agent factory.

        Args:
            telemetry_service: Telemetry service to inject into agents.
            tool_registry: Tool registry to inject into agents.
            prompt_builder: Prompt builder to inject into agents.
            llm_provider: LLM provider to inject into agents.
        """
        self._telemetry_service = telemetry_service
        self._tool_registry = tool_registry
        self._prompt_builder = prompt_builder
        self._llm_provider = llm_provider

    def create_research_agent(self) -> ResearchAgent:
        """Creates a new ResearchAgent.

        Returns:
            An instantiated ResearchAgent.
        """
        return ResearchAgent(self._telemetry_service, self._tool_registry, self._prompt_builder, self._llm_provider)
