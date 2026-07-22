"""Summary request model."""

from dataclasses import dataclass
from agents.research.research_result import ResearchResult

@dataclass(frozen=True)
class SummaryRequest:
    """Represents the complete input to the Summary Agent."""
    research_result: ResearchResult
    summary_style: str
    audience: str
    tone: str
    length: str
    output_format: str
