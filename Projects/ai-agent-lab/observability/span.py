"""Observability span definition."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Span:
    """Represents a discrete execution span for timing and tracing."""

    name: str
    component: str
    trace_id: str
    start_time: float
    end_time: float | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
