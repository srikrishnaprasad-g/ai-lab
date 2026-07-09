"""Agent result definition."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentResult:
    """Container for the output of an agent execution.

    Attributes:
        success: Whether the agent execution completed successfully.
        output: The resulting data produced by the agent.
        metadata: Telemetry, routing details, or additional execution context.
        errors: A list of string error messages gathered during execution.
    """

    success: bool
    output: Any
    metadata: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
