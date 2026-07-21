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

        Args:
            callback: The final action to perform after all stages.
            args: Positional arguments for the execution.
            kwargs: Keyword arguments for the execution.

        Returns:
            The result of the pipeline execution.
        """
        def _chain(idx: int) -> Callable[..., Any]:
            if idx >= len(self._stages):
                return callback
            return lambda *a, **k: self._stages[idx].execute(
                _chain(idx + 1), *a, **k
            )
        
        return _chain(0)(*args, **kwargs)
