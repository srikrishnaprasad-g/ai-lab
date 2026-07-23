"""Production summary agent implementation."""

from datetime import datetime
from agents.base_agent import BaseAgent
from agents.agent_result import AgentResult
from agents.agent_capabilities import AgentCapabilities
from agents.summary.models.summary_request import SummaryRequest
from agents.summary.models.core import SummaryResult, Finding, Citation, KnowledgeGap, Observation
from agents.summary.models.enums import ConfidenceLevel, ImportanceLevel
from context.request_context import RequestContext
from observability.telemetry_service import TelemetryService
from prompts.summary_prompt_builder import SummaryPromptBuilder
from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest
from agents.summary.llm_response_parser import LLMResponseParser
import time
import json
import logging

logger = logging.getLogger("pipeline")

class SummaryAgent(BaseAgent):
    """Production summary agent."""

    def __init__(self, telemetry_service: TelemetryService, prompt_builder: SummaryPromptBuilder, llm_provider: LLMProvider) -> None:
        """Initializes the summary agent."""
        capabilities = AgentCapabilities(
            supported_actions=["summarize"],
            supported_tools=[],
            execution_requirements=[]
        )
        super().__init__(
            name="summary_agent",
            description="Performs summarization of research results.",
            telemetry_service=telemetry_service,
            capabilities=capabilities
        )
        self._prompt_builder = prompt_builder
        self._llm_provider = llm_provider

    def _execute(self, context: RequestContext) -> AgentResult:
        """Executes summarization logic."""
        request = context.working_memory.get("summary_request")
        if not isinstance(request, SummaryRequest):
            return AgentResult(success=False, output=None, errors=["SummaryRequest not found in context."])
        
        sources = request.research_result.sources
        if not sources:
            return AgentResult(success=True, output=SummaryResult(
                executive_summary="No data to summarize.",
                key_findings=[],
                knowledge_gaps=[KnowledgeGap(question="Unable to find information", reason="No search results", priority=ImportanceLevel.HIGH)],
                citations=[],
                confidence=ConfidenceLevel.UNKNOWN
            ))
            
        # Using the prompt builder (Task 6.3C)
        search_results_text = "\n".join([f"- {s.title}: {s.snippet}" for s in sources])
        prompt_result = self._prompt_builder.build_summary_prompt(
            topic=request.research_result.original_query,
            search_results=search_results_text,
            tone="professional"
        )
        
        # LLM Invocation
        logger.info(f"[PASS] LLM Provider\nProvider: {self._llm_provider.provider_name()}\nModel: {self._llm_provider._config.model}\nAPI Key: Detected\n\nPrompt Length: {len(prompt_result.prompt)} chars\n\nCalling {self._llm_provider.provider_name()}...")

        start = time.perf_counter()
        llm_request = LLMRequest(
            prompt=prompt_result.prompt,
            system_prompt=prompt_result.system_prompt,
            metadata={"request_id": context.request_id}
        )

        try:
            response = self._llm_provider.generate(llm_request)
            latency = time.perf_counter() - start

            logger.info(f"[PASS] Gemini API\nHTTP Status: 200\nLatency: {latency:.2f} sec\nResponse Length: {len(response.content)} chars")

            # Use dedicated parser/validator
            result = LLMResponseParser.parse_and_validate(response.content)
            
            logger.info(f"[PASS] Summary Agent\nExecutive Summary: {len(result.executive_summary)} chars\nKey Findings: {len(result.key_findings)}\nSummaryResult created.")
            return AgentResult(success=True, output=result)

        except ValueError as e:
            logger.error(f"[FAIL] Summary Agent Validation\nReason: {e}")
            return AgentResult(success=False, output=None, errors=[str(e)])
        except Exception as e:
            logger.error(f"[FAIL] Gemini API\nReason: {e}")
            return AgentResult(success=False, output=None, errors=[str(e)])
