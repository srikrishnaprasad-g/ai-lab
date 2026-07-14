"""Summary prompt builder implementation."""

from prompts.prompt_builder import PromptBuilder
from prompts.prompt_result import PromptResult
from search.search_response import SearchResponse


class SummaryPromptBuilder(PromptBuilder):
    """Constructs prompts for the summary agent."""

    def build(self, search_response: SearchResponse) -> PromptResult:
        """Constructs a summary prompt from the search response."""
        prompt = "Summarize the following search results:\n" + "\n".join(
            [f"- {r.title}: {r.snippet}" for r in search_response.results]
        )
        return PromptResult(prompt=prompt)
