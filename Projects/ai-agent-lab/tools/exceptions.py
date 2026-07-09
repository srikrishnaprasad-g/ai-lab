"""Tool-specific exception definitions."""


class ToolException(Exception):
    """Base exception for all tool-related errors."""
    pass


class ToolExecutionError(ToolException):
    """Raised when a tool fails to execute its task."""
    pass
