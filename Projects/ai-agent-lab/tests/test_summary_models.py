"""Unit tests for summary domain models."""
from datetime import datetime
from agents.summary.models.core import Observation, Citation, Finding, KnowledgeGap, SummaryResult
from agents.summary.models.summary_request import SummaryRequest
from agents.research.research_result import ResearchResult

def test_observation_model():
    obs = Observation(id="1", title="Obs", snippet="Snip", url="http://x", rank=1, provider="test")
    assert obs.id == "1"
    assert obs.title == "Obs"

def test_citation_model():
    cit = Citation(source_id="1", title="Cit", url="http://x", retrieved_at=datetime.now())
    assert cit.source_id == "1"

def test_finding_model():
    obs = Observation(id="1", title="Obs", snippet="Snip", url="http://x", rank=1, provider="test")
    finding = Finding(title="F", description="D", importance=1.0, supporting_observations=[obs], confidence=1.0)
    assert finding.title == "F"
    assert len(finding.supporting_observations) == 1

def test_summary_request_model():
    res = ResearchResult(original_query="q", search_provider="p")
    req = SummaryRequest(research_result=res, summary_style="brief", audience="dev", tone="tech", length="short", output_format="text")
    assert req.summary_style == "brief"
    assert req.research_result.original_query == "q"

if __name__ == "__main__":
    test_observation_model()
    test_citation_model()
    test_finding_model()
    test_summary_request_model()
    print("All summary domain model tests PASSED.")
