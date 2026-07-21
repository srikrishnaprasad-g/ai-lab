"""Execution decision contract."""

from dataclasses import dataclass, field
from typing import Any
from registry.agent_id import AgentId
from runtime.execution_action import ExecutionAction


@dataclass
class ExecutionDecision:
    """Represents a decision made by the planner."""

    action: ExecutionAction
    target: AgentId | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
