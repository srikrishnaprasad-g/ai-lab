"""Execution action identifiers."""

from enum import StrEnum


class ExecutionAction(StrEnum):
    """Enumeration of available execution actions."""

    EXECUTE = "EXECUTE"
    TERMINATE = "TERMINATE"
    WAIT = "WAIT"
