"""Planner abstraction and implementation."""

from abc import ABC, abstractmethod
from context.request_context import RequestContext
from runtime.execution_action import ExecutionAction
from runtime.planner.execution_plan import ExecutionPlan


class Planner(ABC):
    """Abstract base class for planning component."""

    @abstractmethod
    def plan(self, context: RequestContext) -> ExecutionPlan:
        """Determines the next execution action.

        Args:
            context: The request context.

        Returns:
            The execution plan.
        """
        pass


class TaskPlanner(Planner):
    """Concrete implementation of the planner."""

    def plan(self, context: RequestContext) -> ExecutionPlan:
        """Determines the next execution action based on context."""
        # Simple deterministic logic for Task 4.5.1
        # Initially only support EXECUTE action, without routing info.
        return ExecutionPlan(action=ExecutionAction.EXECUTE)
