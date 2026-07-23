"""Workflow definition models."""
from dataclasses import dataclass
from runtime.models.plan import ExecutionPlan
from runtime.orchestrator.task_graph import TaskGraph

@dataclass
class WorkflowDefinition:
    """Defines the structure and strategy of an agent workflow."""
    name: str
    plan: ExecutionPlan
    task_graph: TaskGraph
