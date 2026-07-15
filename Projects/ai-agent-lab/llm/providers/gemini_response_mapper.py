"""Gemini response mapper."""

from typing import Any
from llm.llm_response import LLMResponse


class GeminiResponseMapper:
    """Handles mapping of Gemini REST API responses to LLMResponse."""

    @staticmethod
    def map_response(data: dict[str, Any], model: str) -> LLMResponse:
        """Maps Gemini JSON response to LLMResponse."""
        # Simple placeholder mapping logic as per requirements
        # (Real mapping will be implemented in Task 3.8)
        content = data.get("content", "No content")
        metadata = {
            "finish_reason": data.get("finish_reason"),
            "token_usage": data.get("usageMetadata"),
            "raw_provider_metadata": data,
        }
        
        return LLMResponse(
            content=content,
            model=model,
            provider="gemini",
            metadata=metadata
        )
