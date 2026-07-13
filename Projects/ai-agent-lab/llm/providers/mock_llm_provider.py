"""Mock LLM provider implementation."""

from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest, LLMResponse


class MockLLMProvider(LLMProvider):
    """Deterministic mock implementation of LLM."""

    def provider_name(self) -> str:
        """Returns the name of the provider."""
        return "mock"

    def generate(self, request: LLMRequest) -> LLMResponse:
        """Returns deterministic mock LLM response."""
        return LLMResponse(
            text=f"Mock response for: {request.prompt}",
            model=request.model or "mock-model"
        )
