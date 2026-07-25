"""Smoke test for the ExecutionPipeline framework including RetryStage."""

from typing import Any, Callable
from runtime.pipeline.pipeline_stage import PipelineStage
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from runtime.pipeline.retry_stage import RetryStage

class FailingStage(PipelineStage):
    """A stage that fails n times before succeeding."""
    def __init__(self, fail_n_times: int):
        self.fail_n_times = fail_n_times
        self.attempts = 0

    def execute(self, next_stage: Callable[..., Any], *args, **kwargs) -> Any:
        self.attempts += 1
        if self.attempts <= self.fail_n_times:
            raise ValueError("Simulated failure")
        return next_stage(*args, **kwargs)

def run_smoke_test() -> None:
    """Demonstrates retry behavior in the pipeline."""
    
    # Scenario 1: Success on first attempt
    print("Scenario 1: Testing success path...")
    retry_stage = RetryStage(max_attempts=3, retry_exceptions=(ValueError,))
    pipeline = ExecutionPipeline([retry_stage])
    
    result = pipeline.execute(lambda: "success")
    assert result == "success"
    print("Scenario 1 PASSED.")

    # Scenario 2: Fail once, succeed on second attempt
    print("Scenario 2: Testing retry-then-success...")
    failing_stage = FailingStage(fail_n_times=1)
    pipeline = ExecutionPipeline([retry_stage, failing_stage])
    
    result = pipeline.execute(lambda: "success")
    assert result == "success"
    assert failing_stage.attempts == 2
    print("Scenario 2 PASSED.")

    # Scenario 3: Always fail, propagate exception
    print("Scenario 3: Testing exhaustion...")
    failing_stage = FailingStage(fail_n_times=3)
    pipeline = ExecutionPipeline([retry_stage, failing_stage])
    
    try:
        pipeline.execute(lambda: "success")
        assert False, "Should have raised ValueError"
    except ValueError:
        assert failing_stage.attempts == 3
        print("Scenario 3 PASSED.")

if __name__ == "__main__":
    run_smoke_test()
