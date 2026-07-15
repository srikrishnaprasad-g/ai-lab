"""Groq provider stub."""

from llm.exceptions import LLMException
from llm.llm_provider import BaseLLMProvider
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse


class GroqProvider(BaseLLMProvider):
    """Stub implementation for Groq."""

    def provider_name(self) -> str:
        return "groq"

    def generate(self, request: LLMRequest) -> LLMResponse:
        # TODO: Implement streaming support here in Sprint 5
        raise LLMException("GroqProvider has not yet been implemented.")
