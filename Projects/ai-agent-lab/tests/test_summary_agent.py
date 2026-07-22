"""Unit tests for SummaryAgent."""
from unittest.mock import MagicMock
from agents.summary.summary_agent import SummaryAgent
from agents.summary.models.summary_request import SummaryRequest
from agents.summary.models.core import SummaryResult, Finding, Citation, KnowledgeGap
from agents.summary.models.enums import SummaryStyle, Audience, Tone, OutputFormat, ConfidenceLevel
from agents.research.research_result import ResearchResult
from search.search_result import SearchResult
from context.request_context import RequestContext
from observability.telemetry_service import TelemetryService

def test_summary_agent_successful():
    print("Testing SummaryAgent successful summary...")
    telemetry = MagicMock(spec=TelemetryService)
    agent = SummaryAgent(telemetry)
    
    # Setup request
    src1 = SearchResult(title="T1", url="U1", snippet="Snippet 1", rank=1)
    src2 = SearchResult(title="T2", url="U2", snippet="Snippet 2", rank=2)
    res = ResearchResult(original_query="q", search_provider="p", sources=[src1, src2])
    req = SummaryRequest(research_result=res, summary_style=SummaryStyle.EXECUTIVE, audience=Audience.EXECUTIVE, tone=Tone.FORMAL, length="short", output_format=OutputFormat.MARKDOWN)
    
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test")
    context.working_memory["summary_request"] = req
    
    result = agent.execute(context)
    
    assert result.success is True
    assert isinstance(result.output, SummaryResult)
    # Check behavioral improvements
    assert len(result.output.key_findings) == 2
    assert result.output.key_findings[0].title == "Snippet 1"
    assert len(result.output.key_findings[0].supporting_observations) == 1
    assert result.output.confidence == ConfidenceLevel.MEDIUM
    assert len(result.output.citations) == 2
    print("SummaryAgent successful summary PASSED.")

def test_summary_agent_low_confidence_gap():
    print("Testing SummaryAgent low confidence and gap...")
    telemetry = MagicMock(spec=TelemetryService)
    agent = SummaryAgent(telemetry)
    
    # Setup request with only 1 source
    src = SearchResult(title="T", url="U", snippet="S", rank=1)
    res = ResearchResult(original_query="q", search_provider="p", sources=[src])
    req = SummaryRequest(research_result=res, summary_style=SummaryStyle.EXECUTIVE, audience=Audience.EXECUTIVE, tone=Tone.FORMAL, length="short", output_format=OutputFormat.MARKDOWN)
    
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test")
    context.working_memory["summary_request"] = req
    
    result = agent.execute(context)
    
    assert result.success is True
    assert result.output.confidence == ConfidenceLevel.LOW
    assert len(result.output.knowledge_gaps) == 1
    assert "Single source available" in result.output.knowledge_gaps[0].reason
    print("SummaryAgent low confidence and gap PASSED.")

def test_summary_agent_missing_request():
    print("Testing SummaryAgent missing request...")
    telemetry = MagicMock(spec=TelemetryService)
    agent = SummaryAgent(telemetry)
    
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test")
    # working_memory empty
    
    result = agent.execute(context)
    assert result.success is False
    assert "SummaryRequest not found" in result.errors[0]
    print("SummaryAgent missing request PASSED.")

if __name__ == "__main__":
    test_summary_agent_successful()
    test_summary_agent_low_confidence_gap()
    test_summary_agent_missing_request()
    print("All summary agent tests PASSED.")
