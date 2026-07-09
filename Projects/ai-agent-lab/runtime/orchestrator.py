"""Runtime orchestrator implementation."""

import uuid

from agents.agent_result import AgentResult
from agents.exceptions import AgentExecutionError
from context.request_context import RequestContext
from registry.agent_registry import AgentRegistry
from registry.tool_registry import ToolRegistry
from registry.exceptions import ComponentNotFoundError
from runtime.exceptions import OrchestrationError


class RuntimeOrchestrator:
    """Coordinates the execution flow of agents and tools."""

    def __init__(self, agent_registry: AgentRegistry, tool_registry: ToolRegistry, root_agent: str = "root") -> None:
        """Initializes the orchestrator with required registries.

        Args:
            agent_registry: Registry containing all available agents.
            tool_registry: Registry containing all available tools.
            root_agent: The name of the root agent to invoke.
        """
        self._agent_registry = agent_registry
        self._tool_registry = tool_registry
        self._root_agent = root_agent

    def execute(self, user_request: str) -> AgentResult:
        """Orchestrates the execution of a user request.

        Args:
            user_request: The request string provided by the user.

        Returns:
            The final result of the agent orchestration.

        Raises:
            OrchestrationError: If orchestration fails (e.g., root agent not found).
        """
        # Create request context
        request_id = str(uuid.uuid4())
        correlation_id = str(uuid.uuid4())
        context = RequestContext(
            request_id=request_id,
            correlation_id=correlation_id,
            user_request=user_request,
        )

        # Resolve root agent
        try:
            root_agent = self._agent_registry.get(self._root_agent)
        except ComponentNotFoundError as e:
            raise OrchestrationError(f"Failed to resolve root agent: {e}") from e

        # Invoke root agent
        try:
            return root_agent.execute(context)
        except AgentExecutionError as e:
            raise OrchestrationError(f"Root agent execution failed: {e}") from e
