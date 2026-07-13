"""LLM request model."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LLMRequest:
    """Represents a request to an LLM provider."""

    prompt: str
    model: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
