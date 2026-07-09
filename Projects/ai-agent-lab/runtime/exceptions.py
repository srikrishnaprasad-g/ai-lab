"""Runtime-specific exception definitions."""


class RuntimeException(Exception):
    """Base exception for all runtime-related errors."""
    pass


class OrchestrationError(RuntimeException):
    """Raised when the orchestrator fails to manage the execution flow."""
    pass
