"""Artifact representation."""
from dataclasses import dataclass
from typing import Any


@dataclass
class Artifact:
    """Represents a file, data structure, or object produced during execution."""

    name: str
    artifact_type: str
    content: Any
    mime_type: str
