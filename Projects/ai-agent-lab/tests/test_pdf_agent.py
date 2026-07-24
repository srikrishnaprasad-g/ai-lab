"""Unit tests for PDFAgent."""
from unittest.mock import MagicMock
from pathlib import Path
from agents.pdf.pdf_agent import PDFAgent
from agents.pdf.pdf_generator import PDFGenerator
from agents.summary.models.core import SummaryResult
from context.request_context import RequestContext
from observability.telemetry_service import TelemetryService

def test_pdf_agent_successful():
    telemetry = MagicMock(spec=TelemetryService)
    generator = MagicMock(spec=PDFGenerator)
    generator.generate.return_value = (Path("test.pdf"), 1)
    agent = PDFAgent(telemetry, generator)
    
    summary = SummaryResult(executive_summary="Test", key_findings=[], knowledge_gaps=[], citations=[], confidence=MagicMock())
    
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test")
    context.working_memory["summary_result"] = summary
    
    result = agent.execute(context)
    
    assert result.success is True
    assert result.output.file_path.name == "test.pdf"
    generator.generate.assert_called_once()
    print("PDFAgent test passed.")

if __name__ == "__main__":
    test_pdf_agent_successful()
