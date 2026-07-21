"""Execution pipeline engine."""

from typing import Any, Callable
from runtime.pipeline.pipeline_stage import PipelineStage


class ExecutionPipeline:
    """Engine that manages and executes a chain of PipelineStages."""

    def __init__(self, stages: list[PipelineStage]) -> None:
        """Initializes the pipeline with a list of stages.

        Args:
            stages: The ordered list of pipeline stages to execute.
        """
        self._stages = stages

    def execute(self, callback: Callable[..., Any], *args, **kwargs) -> Any:
        """Executes the pipeline chain, terminating with the final callback.

        The pipeline processes the request through registered stages, finally
        invoking the callback with the provided arguments.

        Args:
            callback: The final action to perform after all pipeline stages.
            *args: Positional arguments to forward to all stages and the callback.
            **kwargs: Keyword arguments to forward to all stages and the callback.

        Returns:
            The result of the final callback execution.
        """
        def _chain(idx: int) -> Callable[..., Any]:
            if idx >= len(self._stages):
                return callback
            return lambda *a, **k: self._stages[idx].execute(
                _chain(idx + 1), *a, **k
            )
        
        return _chain(0)(*args, **kwargs)
