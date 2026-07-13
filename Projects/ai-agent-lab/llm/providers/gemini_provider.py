"""Gemini provider stub."""

from llm.exceptions import LLMException
from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse


class GeminiProvider(LLMProvider):
    """Stub implementation for Gemini."""

    def provider_name(self) -> str:
        return "gemini"

    def generate(self, request: LLMRequest) -> LLMResponse:
        raise LLMException("GeminiProvider has not yet been implemented.")
