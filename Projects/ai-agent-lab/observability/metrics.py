"""Observability metrics definition."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Metric:
    """Represents a metric point grouped by category."""

    category: str  # Runtime, LLM, Search, Tool
    name: str
    value: Any
    metadata: dict[str, Any] = field(default_factory=dict)
