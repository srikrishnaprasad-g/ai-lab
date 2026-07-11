"""Search response model."""

from dataclasses import dataclass, field
from typing import Any
from search.search_result import SearchResult


@dataclass
class SearchResponse:
    """Represents the complete search response from a provider."""

    results: list[SearchResult]
    provider: str
    query: str
    metadata: dict[str, Any] = field(default_factory=dict)
