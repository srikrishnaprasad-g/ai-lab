"""Groq provider stub."""

from llm.exceptions import LLMException
from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse


class GroqProvider(LLMProvider):
    """Stub implementation for Groq."""

    def provider_name(self) -> str:
        return "groq"

    def generate(self, request: LLMRequest) -> LLMResponse:
        raise LLMException("GroqProvider has not yet been implemented.")
