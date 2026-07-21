"""Prompt registry."""
from typing import Dict
from prompts.prompt_template import PromptTemplate

class PromptRegistry:
    """Registry to manage prompt templates."""
    
    def __init__(self) -> None:
        self._templates: Dict[str, PromptTemplate] = {}
        
    def register(self, template: PromptTemplate) -> None:
        """Registers a template."""
        if template.template_id in self._templates:
            raise ValueError(f"Template '{template.template_id}' already registered.")
        self._templates[template.template_id] = template
        
    def get(self, template_id: str) -> PromptTemplate:
        """Retrieves a template."""
        if template_id not in self._templates:
            raise ValueError(f"Template '{template_id}' not found.")
        return self._templates[template_id]
