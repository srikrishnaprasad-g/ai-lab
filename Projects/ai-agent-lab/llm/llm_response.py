"""LLM response model."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LLMResponse:
    """Represents the response from an LLM provider."""

    content: str
    model: str
    provider: str
    metadata: dict[str, Any] = field(default_factory=dict)
