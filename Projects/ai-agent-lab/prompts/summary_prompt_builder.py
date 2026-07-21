"""Summary prompt builder implementation."""
from typing import Dict, Any
from prompts.prompt_builder import PromptBuilder, DefaultPromptBuilder
from prompts.prompt_result import PromptResult
from prompts.prompt_registry import PromptRegistry
from search.search_response import SearchResponse

class SummaryPromptBuilder(PromptBuilder):
    """Constructs prompts for the summary agent."""

    def __init__(self, registry: PromptRegistry) -> None:
        self._builder = DefaultPromptBuilder(registry)

    def build(self, template_id: str, variables: Dict[str, Any]) -> str:
        return self._builder.build(template_id, variables)

    def build_summary_prompt(self, search_response: SearchResponse) -> PromptResult:
        """Constructs a summary prompt from the search response."""
        text = "\n".join([f"- {r.title}: {r.snippet}" for r in search_response.results])
        prompt = self.build("summarization_task", {"text": text, "focus_area": "key findings"})
        return PromptResult(prompt=prompt)
