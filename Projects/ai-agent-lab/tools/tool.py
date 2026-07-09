"""Abstract base class for all tools."""

from abc import ABC, abstractmethod
from tools.tool_result import ToolResult


class Tool(ABC):
    """Abstract base class defining the contract for all tools."""

    @abstractmethod
    def name(self) -> str:
        """Gets the name of the tool.

        Returns:
            The name of the tool as a string.
        """
        pass

    @abstractmethod
    def description(self) -> str:
        """Gets a brief description of the tool's purpose and capabilities.

        Returns:
            A string describing what the tool does.
        """
        pass

    @abstractmethod
    def execute(self, context: "RequestContext") -> ToolResult:
        """Executes the tool's logic using the provided request context.

        Args:
            context: The shared request context containing state, variables, and tools.

        Returns:
            A ToolResult containing the success status, output, metadata, and errors.
        """
        pass
