"""Stub LLM providers."""

from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest, LLMResponse


class GeminiProvider(LLMProvider):
    """Stub implementation for Gemini."""

    def provider_name(self) -> str:
        return "gemini"

    def generate(self, request: LLMRequest) -> LLMResponse:
        return LLMResponse(text="Gemini stub", model=request.model or "gemini-stub")


class GroqProvider(LLMProvider):
    """Stub implementation for Groq."""

    def provider_name(self) -> str:
        return "groq"

    def generate(self, request: LLMRequest) -> LLMResponse:
        return LLMResponse(text="Groq stub", model=request.model or "groq-stub")


class OpenRouterProvider(LLMProvider):
    """Stub implementation for OpenRouter."""

    def provider_name(self) -> str:
        return "openrouter"

    def generate(self, request: LLMRequest) -> LLMResponse:
        return LLMResponse(text="OpenRouter stub", model=request.model or "openrouter-stub")
