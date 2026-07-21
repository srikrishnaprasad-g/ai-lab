"""Pipeline stage abstraction."""

from abc import ABC, abstractmethod
from typing import Any, Callable


class PipelineStage(ABC):
    """Abstract base class for execution pipeline stages."""

    @abstractmethod
    def execute(self, next_stage: Callable[..., Any], *args, **kwargs) -> Any:
        """Executes the stage logic.

        Args:
            next_stage: The next stage or final callback in the pipeline.
            args: Positional arguments for the execution.
            kwargs: Keyword arguments for the execution.

        Returns:
            The result of the execution.
        """
        pass
