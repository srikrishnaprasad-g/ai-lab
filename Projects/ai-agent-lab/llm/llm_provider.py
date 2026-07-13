"""LLM provider abstraction."""

from abc import ABC, abstractmethod
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse


class LLMProvider(ABC):
    """Abstract base class defining the contract for all LLM providers."""

    @abstractmethod
    def generate(self, request: LLMRequest) -> LLMResponse:
        """Generates a response from the LLM."""
        pass

    @abstractmethod
    def provider_name(self) -> str:
        """Returns the name of the provider."""
        pass
