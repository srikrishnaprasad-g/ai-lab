"""Summary request model."""

from dataclasses import dataclass
from agents.research.research_result import ResearchResult
from agents.summary.models.enums import SummaryStyle, Audience, Tone, OutputFormat

@dataclass(frozen=True)
class SummaryRequest:
    """Represents the complete input to the Summary Agent."""
    research_result: ResearchResult
    summary_style: SummaryStyle
    audience: Audience
    tone: Tone
    length: str
    output_format: OutputFormat
