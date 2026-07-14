"""Runtime orchestrator implementation."""

import uuid

from agents.agent_result import AgentResult
from agents.exceptions import AgentExecutionError
from context.request_context import RequestContext
from registry.agent_registry import AgentRegistry
from registry.tool_registry import ToolRegistry
from registry.exceptions import ComponentNotFoundError
from runtime.exceptions import OrchestrationError
from runtime.runtime_result import RuntimeResult
from observability.telemetry_service import TelemetryService


class RuntimeOrchestrator:
    """Coordinates the execution flow of agents and tools."""

    def __init__(self, agent_registry: AgentRegistry, tool_registry: ToolRegistry, telemetry_service: TelemetryService, root_agent: str = "root") -> None:
        """Initializes the orchestrator with required registries and telemetry.

        Args:
            agent_registry: Registry containing all available agents.
            tool_registry: Registry containing all available tools.
            telemetry_service: The telemetry service for instrumentation.
            root_agent: The name of the root agent to invoke.
        """
        self._agent_registry = agent_registry
        self._tool_registry = tool_registry
        self._telemetry_service = telemetry_service
        self._root_agent = root_agent

    def execute(self, user_request: str) -> RuntimeResult:
        """Orchestrates the execution of a user request.

        Args:
            user_request: The request string provided by the user.

        Returns:
            The complete runtime result containing context and agent result.

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

        # Start span for orchestration
        span = self._telemetry_service.start_span("orchestrate", component="orchestrator", trace_id=correlation_id)

        try:
            # Resolve root agent
            try:
                root_agent = self._agent_registry.get(self._root_agent)
            except ComponentNotFoundError as e:
                raise OrchestrationError(f"Failed to resolve root agent: {e}") from e

            # Invoke root agent
            try:
                result = root_agent.execute(context)
                return RuntimeResult(context=context, result=result)
            except AgentExecutionError as e:
                raise OrchestrationError(f"Root agent execution failed: {e}") from e
        finally:
            self._telemetry_service.end_span(span)
