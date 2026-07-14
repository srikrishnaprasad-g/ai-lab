"""Prompt result definition."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PromptResult:
    """Carries the generated prompt, system prompt, and metadata."""

    prompt: str
    system_prompt: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
