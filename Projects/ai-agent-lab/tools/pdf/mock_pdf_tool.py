"""Mock PDF tool implementation."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from tools.tool import Tool
from tools.tool_result import ToolResult
from context.artifact import Artifact
from context.execution_event import ExecutionEvent
from context import keys

if TYPE_CHECKING:
    from context.request_context import RequestContext


class MockPDFTool(Tool):
    """A deterministic mock implementation of a PDF generation tool."""

    def name(self) -> str:
        """Gets the name of the tool."""
        return "mock_pdf_tool"

    def description(self) -> str:
        """Gets a brief description of the tool's purpose."""
        return "Simulates PDF generation from a summary."

    def execute(self, context: "RequestContext") -> ToolResult:
        """Executes the mock PDF generation."""
        summary = context.working_memory.get(keys.FINAL_SUMMARY, "No summary available.")

        # Create artifact
        artifact = Artifact(
            name="research_summary.pdf",
            artifact_type="pdf",
            content=summary,
            mime_type="application/pdf",
        )
        context.artifacts.append(artifact)

        # Append execution event
        event = ExecutionEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            component=self.name(),
            component_type="tool",
            event_type="completed",
            details={"artifact_name": artifact.name},
            duration_ms=0.0,
        )
        context.execution_trace.append(event)

        return ToolResult(
            success=True,
            output=artifact.name,
            metadata={
                "tool": self.name(),
                "artifact_type": artifact.artifact_type,
                "source": "mock"
            }
        )
