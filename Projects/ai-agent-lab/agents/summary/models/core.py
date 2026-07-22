"""Models for the Summary Agent."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Optional
from search.search_result import SearchResult

@dataclass(frozen=True)
class Observation:
    """Represents one normalized research observation."""
    id: str
    title: str
    snippet: str
    url: str
    rank: int
    provider: str
    retrieved_at: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class Citation:
    """Represents a citation used in generated summaries."""
    source_id: str
    title: str
    url: str
    retrieved_at: datetime
    used_by: List[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class Finding:
    """Represents one synthesized insight."""
    title: str
    description: str
    importance: float
    supporting_observations: List[Observation]
    confidence: float

@dataclass(frozen=True)
class KnowledgeGap:
    """Represents missing or uncertain information."""
    question: str
    reason: str
    priority: int
    recommended_search: Optional[str] = None

@dataclass(frozen=True)
class SummaryResult:
    """Represents the structured output of the Summary Agent."""
    executive_summary: str
    key_findings: List[Finding]
    knowledge_gaps: List[KnowledgeGap]
    citations: List[Citation]
    confidence: float
    metadata: dict[str, Any] = field(default_factory=dict)
