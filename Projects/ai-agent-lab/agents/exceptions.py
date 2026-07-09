"""Agent-specific exception definitions."""


class AgentException(Exception):
    """Base exception for all agent-related errors."""
    pass


class AgentExecutionError(AgentException):
    """Raised when an agent fails to execute its task."""
    pass
