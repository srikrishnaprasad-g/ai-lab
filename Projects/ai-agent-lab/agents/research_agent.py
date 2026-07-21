"""Production research agent implementation."""

from registry.tool_registry import ToolRegistry
from prompts.prompt_builder import PromptBuilder
from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest
from context.request_context import RequestContext
from agents.agent_result import AgentResult
from agents.base_agent import BaseAgent
from agents.agent_capabilities import AgentCapabilities
from observability.telemetry_service import TelemetryService
from context import keys

class ResearchAgent(BaseAgent):
    """Production research agent."""

    def __init__(self, telemetry_service: TelemetryService, tool_registry: ToolRegistry, prompt_builder: PromptBuilder, llm_provider: LLMProvider) -> None:
        """Initializes the research agent."""
        self._tool_registry = tool_registry
        self._prompt_builder = prompt_builder
        self._llm_provider = llm_provider
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
        tool = self._tool_registry.get("web_search")
        tool_result = tool.execute(context)
        
        if not tool_result.success:
            return AgentResult(success=False, output="Search failed")
            
        search_response = context.working_memory.get(keys.SEARCH_RESPONSE)
        if not search_response:
             return AgentResult(success=False, output="Search response missing")
        
        # Build prompt using PromptBuilder
        prompt = self._prompt_builder.build("research_task", {"topic": context.user_request, "format": "summary"})
        
        # Call LLM Provider
        llm_response = self._llm_provider.generate(LLMRequest(prompt=prompt, model="default-model"))
        
        return AgentResult(success=True, output=llm_response.content)
