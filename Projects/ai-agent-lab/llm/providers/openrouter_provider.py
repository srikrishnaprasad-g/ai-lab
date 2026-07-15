"""OpenRouter provider stub."""

from llm.exceptions import LLMException
from llm.llm_provider import BaseLLMProvider
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse


class OpenRouterProvider(BaseLLMProvider):
    """Stub implementation for OpenRouter."""

    def provider_name(self) -> str:
        return "openrouter"

    def generate(self, request: LLMRequest) -> LLMResponse:
        # TODO: Implement streaming support here in Sprint 5
        raise LLMException("OpenRouterProvider has not yet been implemented.")

