"""Prompt builder abstraction."""

from abc import ABC, abstractmethod
from prompts.prompt_result import PromptResult
from search.search_response import SearchResponse


class PromptBuilder(ABC):
    """Abstract base class for constructing prompts."""

    @abstractmethod
    def build(self, search_response: SearchResponse) -> PromptResult:
        """Constructs a prompt based on the provided search response.

        Args:
            search_response: The search response to process.

        Returns:
            A PromptResult containing the formatted prompt.
        """
        pass
