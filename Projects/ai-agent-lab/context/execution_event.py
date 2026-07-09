"""Execution event representation."""
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class ExecutionEvent:
    """Represents a discrete event that occurred during runtime execution."""

    event_id: str
    timestamp: datetime
    component: str
    component_type: str
    event_type: str
    details: dict[str, Any]
    duration_ms: float | None = None
