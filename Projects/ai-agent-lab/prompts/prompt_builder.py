"""Prompt builder interface."""
from abc import ABC, abstractmethod
from typing import Dict, Any
from prompts.prompt_registry import PromptRegistry
from prompts.prompt_renderer import PromptRenderer
from prompts.prompt_variables import PromptVariables

class PromptBuilder(ABC):
    """Abstract interface for agents to request rendered prompts."""
    
    @abstractmethod
    def build(self, template_id: str, variables: Dict[str, Any]) -> str:
        """Builds a rendered prompt."""
        pass

class DefaultPromptBuilder(PromptBuilder):
    """Production implementation of PromptBuilder."""
    
    def __init__(self, registry: PromptRegistry) -> None:
        self._registry = registry
        self._renderer = PromptRenderer()
        
    def build(self, template_id: str, variables: Dict[str, Any]) -> str:
        """Builds a rendered prompt."""
        template = self._registry.get(template_id)
        prompt_vars = PromptVariables(variables)
        return self._renderer.render(template, prompt_vars)
