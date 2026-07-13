"""OpenRouter provider stub."""

from llm.exceptions import LLMException
from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse


class OpenRouterProvider(LLMProvider):
    """Stub implementation for OpenRouter."""

    def provider_name(self) -> str:
        return "openrouter"

    def generate(self, request: LLMRequest) -> LLMResponse:
        raise LLMException("OpenRouterProvider has not yet been implemented.")
