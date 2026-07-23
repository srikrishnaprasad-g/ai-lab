"""Typed context container extending RequestContext for orchestrator state."""
from dataclasses import dataclass
from typing import Any, TypeVar, Type, Optional
from context.request_context import RequestContext

T = TypeVar("T")

@dataclass
class TypedWorkflowContext(RequestContext):
    """Strongly typed container for workflow execution state, extending RequestContext."""

    def set(self, key: str, value: Any) -> None:
        self.working_memory[key] = value

    def get(self, key: str, expected_type: Type[T]) -> Optional[T]:
        value = self.working_memory.get(key)
        if value is not None and expected_type is not Any and not isinstance(value, expected_type):
            raise TypeError(f"Key '{key}' expected {expected_type}, got {type(value)}")
        return value
    
    def has(self, key: str) -> bool:
        return key in self.working_memory
