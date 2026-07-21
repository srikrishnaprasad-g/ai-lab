"""Runtime bootstrap implementation."""

from runtime.runtime_orchestrator import RuntimeOrchestrator
from runtime.planner.planner import TaskPlanner
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from runtime.pipeline.telemetry_stage import TelemetryStage
from runtime.pipeline.retry_stage import RetryStage
from observability.telemetry_service import TelemetryService


class RuntimeBootstrap:
    """Composition root for the runtime components."""

    @staticmethod
    def build() -> RuntimeOrchestrator:
        """Constructs and wires the runtime components.

        Returns:
            A fully configured RuntimeOrchestrator instance.
        """
        # 1. Telemetry
        telemetry_service = TelemetryService()
        
        # 2. Pipeline Stages
        telemetry_stage = TelemetryStage(telemetry_service)
        retry_stage = RetryStage(max_attempts=3, retry_exceptions=(Exception,))
        
        # 3. Pipeline
        pipeline = ExecutionPipeline([telemetry_stage, retry_stage])
        
        # 4. Planner
        planner = TaskPlanner()
        
        # 5. Orchestrator
        orchestrator = RuntimeOrchestrator(planner, pipeline)
        
        return orchestrator
