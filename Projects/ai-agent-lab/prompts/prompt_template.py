"""Prompt template definition."""
from dataclasses import dataclass, field
from typing import Set

@dataclass(frozen=True)
class PromptTemplate:
    """Immutable prompt template definition."""
    template_id: str
    description: str
    version: str
    template_string: str
    required_variables: Set[str] = field(default_factory=set)
