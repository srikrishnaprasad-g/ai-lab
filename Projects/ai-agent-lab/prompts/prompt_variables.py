"""Prompt variables container."""
from typing import Any, Dict, Mapping
from types import MappingProxyType

class PromptVariables:
    """Strongly typed container for prompt variables."""
    def __init__(self, variables: Dict[str, Any]) -> None:
        # Use MappingProxyType for immutability
        self._variables = MappingProxyType(variables.copy())

    def get_all(self) -> Mapping[str, Any]:
        return self._variables
    
    def validate(self, required_keys: set[str]) -> None:
        """Validates that all required variables are present."""
        missing = required_keys - set(self._variables.keys())
        if missing:
            raise ValueError(f"Missing required variables: {missing}")
