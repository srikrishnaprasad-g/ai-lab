"""Runtime orchestrator implementation."""

from typing import Any, Callable
from context.request_context import RequestContext
from runtime.planner.planner import Planner
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from registry.agent_registry import AgentRegistry
from runtime.execution_action import ExecutionAction
from runtime.exceptions import OrchestrationError

class RuntimeOrchestrator:
    """Coordinates planning and execution."""

    def __init__(self, planner: Planner, pipeline: ExecutionPipeline, agent_registry: AgentRegistry) -> None:
        """Initializes the orchestrator with required dependencies.

        Args:
            planner: The planner component.
            pipeline: The execution pipeline component.
            agent_registry: The agent registry.
        """
        self._planner = planner
        self._pipeline = pipeline
        self._agent_registry = agent_registry

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

    def get_agent(self, agent_name: str) -> Any:
        """Retrieves an agent from the registry.
        
        Args:
            agent_name: Name of the agent.
            
        Returns:
            The agent instance.
            
        Raises:
            OrchestrationError: If agent not found.
        """
        try:
            return self._agent_registry.get(agent_name)
        except Exception as e:
            raise OrchestrationError(f"Agent '{agent_name}' not found.") from e
