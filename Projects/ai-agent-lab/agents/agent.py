"""Abstract base class for all agents."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from agents.agent_result import AgentResult

if TYPE_CHECKING:
    # Future import when RequestContext exists in Task 2.3
    # from context.request_context import RequestContext
    pass


class Agent(ABC):
    """Abstract base class defining the contract for all agents."""

    @abstractmethod
    def name(self) -> str:
        """Gets the name of the agent.

        Returns:
            The name of the agent as a string.
        """
        pass

    @abstractmethod
    def description(self) -> str:
        """Gets a brief description of the agent's purpose and capabilities.

        Returns:
            A string describing what the agent does.
        """
        pass

    @abstractmethod
    def execute(self, context: "RequestContext") -> AgentResult:
        """Executes the agent's logic using the provided request context.

        Args:
            context: The shared request context containing state, variables, and tools.

        Returns:
            An AgentResult containing the success status, output, metadata, and errors.
        """
        pass
