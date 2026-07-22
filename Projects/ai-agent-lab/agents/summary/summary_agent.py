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

class SummaryAgent(BaseAgent):
    """Production summary agent."""

    def __init__(self, telemetry_service: TelemetryService, prompt_builder: SummaryPromptBuilder) -> None:
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
        
        # NOTE: LLM integration is planned for future sprint.
        # For now, we simulate the result using the rendered prompt.
        
        observations = [
            Observation(
                id=f"obs_{i}",
                title=s.title,
                snippet=s.snippet,
                url=s.url,
                rank=s.rank,
                provider=request.research_result.search_provider
            ) for i, s in enumerate(sources)
        ]
        
        # Synthesize Findings and Citations
        findings = []
        citations = []
        for i, obs in enumerate(observations):
            # Deterministic Finding Title: First 3 words of snippet
            words = obs.snippet.split()
            title = " ".join(words[:3]).capitalize() if words else f"Finding {i+1}"
            
            findings.append(Finding(
                title=title,
                description=obs.snippet,
                importance=ImportanceLevel.MEDIUM,
                supporting_observations=[obs],
                confidence=ConfidenceLevel.HIGH
            ))
            
            # Create citation
            citations.append(Citation(
                source_id=obs.id,
                title=obs.title,
                url=obs.url,
                retrieved_at=obs.retrieved_at
            ))
        
        # Confidence logic
        confidence = ConfidenceLevel.HIGH if len(sources) > 3 else (ConfidenceLevel.LOW if len(sources) == 1 else ConfidenceLevel.MEDIUM)
        
        # Knowledge gap logic
        knowledge_gaps = []
        if len(sources) == 1:
            knowledge_gaps.append(KnowledgeGap(question="Insufficient evidence", reason="Single source available", priority=ImportanceLevel.LOW))

        result = SummaryResult(
            executive_summary=f"Analysis of {request.research_result.original_query}: Based on {len(sources)} sources, the key findings highlight {findings[0].title if findings else 'several insights'}.",
            key_findings=findings,
            knowledge_gaps=knowledge_gaps,
            citations=citations,
            confidence=confidence
        )
        
        # AgentResult now contains the telemetry context from the prompt builder indirectly
        return AgentResult(success=True, output=result)
