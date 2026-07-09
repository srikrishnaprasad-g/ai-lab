"""Request context definition."""
from dataclasses import dataclass, field
from typing import Any

from context.artifact import Artifact
from context.execution_event import ExecutionEvent


@dataclass
class RequestContext:
    """Shared execution context passed through agents and tools."""

    request_id: str
    correlation_id: str
    user_request: str
    working_memory: dict[str, Any] = field(default_factory=dict)
    artifacts: list[Artifact] = field(default_factory=list)
    execution_trace: list[ExecutionEvent] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
