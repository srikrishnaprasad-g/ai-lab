"""Runtime package initialization."""

# Explicitly export the public API
from runtime.exceptions import RuntimeException, OrchestrationError
from runtime.runtime_result import RuntimeResult
from runtime.execution_action import ExecutionAction
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from runtime.pipeline.pipeline_stage import PipelineStage

# RuntimeOrchestrator and RuntimeBootstrap are imported lazily when needed
# to avoid eager loading of heavy dependencies (like LLM/Search frameworks).

__all__ = [
    "RuntimeException", 
    "OrchestrationError", 
    "RuntimeResult", 
    "ExecutionAction",
    "ExecutionPipeline",
    "PipelineStage"
]
