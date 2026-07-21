"""Agent result definition."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentResult:
    """Container for the output of an agent execution (Domain Results only).

    Attributes:
        success: Whether the agent execution completed successfully.
        output: The resulting data produced by the agent.
        metadata: Domain-specific execution metadata.
    """

    success: bool
    output: Any
    metadata: dict[str, Any] = field(default_factory=dict)
