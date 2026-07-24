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
        logger.debug(f"Calling {self._llm_provider.provider_name()} with model {self._llm_provider._config.model}. Prompt length: {len(prompt_result.prompt)} chars")

        start = time.perf_counter()
        llm_request = LLMRequest(
            prompt=prompt_result.prompt,
            system_prompt=prompt_result.system_prompt,
            metadata={"request_id": context.request_id}
        )

        try:
            response = self._llm_provider.generate(llm_request)
            latency = time.perf_counter() - start

            logger.debug(f"[PASS] Gemini API\nHTTP Status: 200\nLatency: {latency:.2f} sec\nResponse Length: {len(response.content)} chars")

            # Use dedicated parser/validator
            result = LLMResponseParser.parse_and_validate(response.content)
            
            # Store provider in metadata for PDF Agent to access
            result.metadata["provider"] = self._llm_provider.provider_name()
            
            # Store detailed metrics in context working memory for verbose reporting
            context.working_memory["summary_metrics"] = {
                "provider": self._llm_provider.provider_name(),
                "model": self._llm_provider._config.model,
                "prompt_length": len(prompt_result.prompt),
                "response_length": len(response.content),
                "latency": latency,
                "status_code": 200
            }
            
            return AgentResult(success=True, output=result)

        except ValueError as e:
            logger.error(f"[FAIL] Summary Agent Validation\nReason: {e}")
            return AgentResult(success=False, output=None, errors=[str(e)])
        except Exception as e:
            logger.error(f"[FAIL] Gemini API\nReason: {e}")
            return AgentResult(success=False, output=None, errors=[str(e)])
