"""Summary prompt builder implementation."""
from typing import Dict, Any
from prompts.prompt_builder import PromptBuilder
from prompts.prompt_result import PromptResult
from prompts.prompt_registry import PromptRegistry
from prompts.prompt_renderer import PromptRenderer
from prompts.prompt_variables import PromptVariables
from prompts.templates import SUMMARIZATION_SYSTEM_V1, SUMMARIZATION_USER_V1

class SummaryPromptBuilder(PromptBuilder):
    """Constructs production-ready prompts for the summary agent."""

    def __init__(self, registry: PromptRegistry) -> None:
        self._registry = registry
        self._renderer = PromptRenderer()
        self._registry.register(SUMMARIZATION_SYSTEM_V1)
        self._registry.register(SUMMARIZATION_USER_V1)

    def build(self, template_id: str, variables: Dict[str, Any]) -> str:
        """Required implementation of PromptBuilder.build."""
        template = self._registry.get(template_id)
        return self._renderer.render(template, PromptVariables(variables))

    def build_summary_prompt(
        self, topic: str, search_results: str, tone: str = "professional", context: str = ""
    ) -> PromptResult:
        """Constructs system and user prompts."""
        
        system_template = self._registry.get(SUMMARIZATION_SYSTEM_V1.template_id)
        user_template = self._registry.get(SUMMARIZATION_USER_V1.template_id)
        
        system_prompt = self._renderer.render(system_template, PromptVariables({}))
        user_prompt = self._renderer.render(user_template, PromptVariables({
            "topic": topic,
            "search_results": search_results,
            "tone": tone,
            "context": context
        }))
        
        # NOTE: Returning combined prompt as per PromptResult definition in Sprint 4
        return PromptResult(prompt=f"System: {system_prompt}\n\nUser: {user_prompt}")
