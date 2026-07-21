"""Retry pipeline stage implementation."""

from typing import Any, Callable
from runtime.pipeline.pipeline_stage import PipelineStage


class RetryStage(PipelineStage):
    """Pipeline stage that retries execution on retryable failures."""

    def __init__(self, max_attempts: int, retry_exceptions: tuple[type[Exception], ...]) -> None:
        """Initializes the retry stage.

        Args:
            max_attempts: Maximum number of execution attempts.
            retry_exceptions: Tuple of exception types that trigger a retry.

        Raises:
            ValueError: If max_attempts is less than 1.
        """
        if max_attempts < 1:
            raise ValueError("max_attempts must be >= 1")
        self._max_attempts = max_attempts
        self._retry_exceptions = retry_exceptions

    def execute(self, next_stage: Callable[..., Any], *args, **kwargs) -> Any:
        """Executes the pipeline stage, retrying if the downstream stage fails."""
        for attempt in range(1, self._max_attempts + 1):
            try:
                return next_stage(*args, **kwargs)
            except self._retry_exceptions:
                if attempt == self._max_attempts:
                    raise
        return None # Should not be reached
