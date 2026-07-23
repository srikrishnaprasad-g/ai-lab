"""Execution planning models."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any
from runtime.models.policy import ExecutionPolicy

@dataclass
class ExecutionPlan:
    """Strategy for orchestrating workflow execution."""
    policy: ExecutionPolicy = field(default_factory=ExecutionPolicy)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)
