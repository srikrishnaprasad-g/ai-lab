"""Execution policy definitions."""
from dataclasses import dataclass
from typing import Tuple, Type

@dataclass(frozen=True)
class ExecutionPolicy:
    """Encapsulates retry and failure behaviors."""
    max_retries: int = 3
    timeout_seconds: int = 30
    retry_exceptions: Tuple[Type[Exception], ...] = (Exception,)
