"""Runtime orchestrator implementation."""

from typing import Any, Callable
from context.request_context import RequestContext
from runtime.planner.planner import Planner
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from runtime.execution_action import ExecutionAction
from runtime.exceptions import OrchestrationError

class RuntimeOrchestrator:
    """Coordinates planning and execution."""

    def __init__(self, planner: Planner, pipeline: ExecutionPipeline) -> None:
        """Initializes the orchestrator with required dependencies.

        Args:
            planner: The planner component.
            pipeline: The execution pipeline component.
        """
        self._planner = planner
        self._pipeline = pipeline

    def execute(self, context: RequestContext, callback: Callable[..., Any]) -> Any:
        """Orchestrates the planning and execution of a request.

        Args:
            context: The request context.
            callback: The final callback to execute after the pipeline.

        Returns:
            The result of the callback.

        Raises:
            OrchestrationError: If the plan action is unsupported.
        """
        # 1. Planner.plan(context)
        plan = self._planner.plan(context)
        
        # 2. Validate plan
        if plan.action != ExecutionAction.EXECUTE:
            raise OrchestrationError(f"Unsupported action: {plan.action}")
            
        # 3. ExecutionPipeline.execute(callback)
        # Passing context to the pipeline to be used by stages and the callback
        return self._pipeline.execute(callback, context)
