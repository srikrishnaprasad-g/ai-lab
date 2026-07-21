"""Base class for production agents."""

import logging
from abc import ABC, abstractmethod
from context.request_context import RequestContext
from agents.agent import Agent
from agents.agent_result import AgentResult
from observability.telemetry_service import TelemetryService
from agents.agent_capabilities import AgentCapabilities

logger = logging.getLogger(__name__)

class BaseAgent(Agent, ABC):
    """Base class providing reusable agent lifecycle behavior."""

    def __init__(self, name: str, description: str, telemetry_service: TelemetryService, capabilities: AgentCapabilities) -> None:
        """Initializes the base agent.

        Args:
            name: Agent name.
            description: Agent purpose.
            telemetry_service: Telemetry service for instrumentation.
            capabilities: Agent capabilities description.
        """
        self._name = name
        self._description = description
        self._telemetry = telemetry_service
        self._capabilities = capabilities

    def name(self) -> str:
        return self._name

    def description(self) -> str:
        return self._description

    @property
    def capabilities(self) -> AgentCapabilities:
        return self._capabilities

    @abstractmethod
    def _execute(self, context: RequestContext) -> AgentResult:
        """Internal execution logic to be implemented by concrete agents."""
        pass

    def execute(self, context: RequestContext) -> AgentResult:
        """Executes the agent's logic with telemetry and error handling."""
        logger.info(f"Agent {self._name} executing for request {context.request_id}")
        
        span = self._telemetry.start_span(
            name=f"agent_execute_{self._name}",
            component=self._name,
            trace_id=context.request_id
        )
        
        try:
            result = self._execute(context)
            
            if result.success:
                logger.info(f"Agent {self._name} execution succeeded.")
            else:
                logger.error(f"Agent {self._name} execution failed: {result.errors}")
                
            return result
        except Exception as e:
            logger.exception(f"Agent {self._name} encountered unexpected error: {e}")
            raise
        finally:
            self._telemetry.end_span(span)
