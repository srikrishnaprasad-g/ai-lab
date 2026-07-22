"""Structured research result."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from search.search_result import SearchResult

@dataclass
class ResearchResult:
    """Represents a normalized research result."""
    original_query: str
    search_provider: str
    search_timestamp: datetime = field(default_factory=datetime.now)
    source_count: int = 0
    sources: list[SearchResult] = field(default_factory=list)
    observations: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    processing_duration: float | None = None
    raw_search_response: Any = None
