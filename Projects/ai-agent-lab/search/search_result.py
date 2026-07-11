"""Search result model."""

from dataclasses import dataclass


@dataclass
class SearchResult:
    """Represents a single search result."""

    title: str
    url: str
    snippet: str
    rank: int
