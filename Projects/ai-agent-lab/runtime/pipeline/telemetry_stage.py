"""Telemetry pipeline stage implementation."""

import uuid
from typing import Any, Callable

from observability.telemetry_service import TelemetryService
from runtime.pipeline.pipeline_stage import PipelineStage
from context.request_context import RequestContext

class TelemetryStage(PipelineStage):
    """Pipeline stage that captures execution telemetry."""

    def __init__(self, telemetry_service: TelemetryService) -> None:
        """Initializes the telemetry stage.

        Args:
            telemetry_service: The service to record telemetry.
        """
        self._telemetry_service = telemetry_service

    def execute(self, next_stage: Callable[..., Any], *args, **kwargs) -> Any:
        """Executes the pipeline stage, wrapping it in telemetry spans."""
        # Extract context if present to get trace_id
        context = next((arg for arg in args if isinstance(arg, RequestContext)), kwargs.get("context"))
        trace_id = context.request_id if isinstance(context, RequestContext) else str(uuid.uuid4())
        
        # Start Span
        span = self._telemetry_service.start_span(
            name="pipeline_stage", 
            component="telemetry_stage", 
            trace_id=trace_id
        )

        try:
            # Invoke next stage
            result = next_stage(*args, **kwargs)
            
            # Record success
            self._telemetry_service.record_metric(
                category="Runtime",
                name="execution_success",
                value=True,
                metadata={"component": "pipeline_stage"}
            )
            return result
        except Exception as e:
            # Record failure
            self._telemetry_service.record_metric(
                category="Runtime",
                name="execution_failure",
                value=str(type(e).__name__),
                metadata={"component": "pipeline_stage"}
            )
            raise
        finally:
            # Always finalize
            self._telemetry_service.end_span(span)
