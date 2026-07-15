"""Mock LLM provider implementation."""

from llm.llm_provider import BaseLLMProvider
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse


class MockLLMProvider(BaseLLMProvider):
    """Deterministic mock implementation of LLM."""

    def provider_name(self) -> str:
        """Returns the name of the provider."""
        return "mock"

    def generate(self, request: LLMRequest) -> LLMResponse:
        """Returns deterministic mock LLM response."""
        return LLMResponse(
            content=f"Mock response for: {request.prompt}",
            model=request.model or "mock-model",
            provider=self.provider_name(),
            metadata={
                "provider": self.provider_name(),
                "model": request.model or "mock-model",
            }
        )
