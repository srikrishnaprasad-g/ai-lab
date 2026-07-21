"""Agent capabilities model."""

from dataclasses import dataclass, field

@dataclass(frozen=True)
class AgentCapabilities:
    """Describes the capabilities of an agent."""

    supported_actions: list[str] = field(default_factory=list)
    supported_tools: list[str] = field(default_factory=list)
    execution_requirements: list[str] = field(default_factory=list)
