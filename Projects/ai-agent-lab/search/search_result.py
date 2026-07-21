"""Search result model."""

from dataclasses import dataclass, field
from typing import Any

@dataclass
class SearchResult:
    """Represents a single search result."""

    title: str
    url: str
    snippet: str
    rank: int
    metadata: dict[str, Any] = field(default_factory=dict)
