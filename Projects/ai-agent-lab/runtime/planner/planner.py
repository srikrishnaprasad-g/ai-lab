"""Planner abstraction and implementation."""

from abc import ABC, abstractmethod
from runtime.models.workflow import WorkflowDefinition
from runtime.models.plan import ExecutionPlan
from runtime.models.policy import ExecutionPolicy
from runtime.orchestrator.task_graph import TaskGraph, TaskNode
from context.request_context import RequestContext

class Planner(ABC):
    """Abstract base class for planning component."""

    @abstractmethod
    def plan(self, context: RequestContext) -> WorkflowDefinition:
        """Determines the workflow definition.

        Args:
            context: The request context.

        Returns:
            The workflow definition.
        """
        pass


class TaskPlanner(Planner):
    """Concrete implementation of the planner."""

    def plan(self, context: RequestContext) -> WorkflowDefinition:
        """Determines the workflow definition based on context."""
        
        # Build Task Graph: Sequential Research -> Summary -> PDF
        graph = TaskGraph()
        graph.add_task(TaskNode(agent_id="research_agent"))
        graph.add_task(TaskNode(agent_id="summary_agent", dependencies=["research_agent"]))
        graph.add_task(TaskNode(agent_id="pdf_agent", dependencies=["summary_agent"]))
        
        # Default Plan/Policy
        plan = ExecutionPlan(policy=ExecutionPolicy(max_retries=2))
        
        return WorkflowDefinition(
            name="research_to_pdf_workflow",
            plan=plan,
            task_graph=graph
        )
