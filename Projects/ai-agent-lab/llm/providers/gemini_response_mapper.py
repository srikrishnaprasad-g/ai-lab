"""Gemini response mapper."""

from typing import Any
from llm.llm_response import LLMResponse
from llm.exceptions import LLMResponseParseError


class GeminiResponseMapper:
    """Handles mapping of Gemini REST API responses to LLMResponse."""

    @staticmethod
    def map_response(data: dict[str, Any], model: str) -> LLMResponse:
        """Maps Gemini JSON response to LLMResponse."""
        try:
            candidates = data.get("candidates", [])
            if not candidates:
                raise LLMResponseParseError("No candidates in response")

            candidate = candidates[0]
            content = candidate.get("content", {}).get("parts", [{}])[0].get("text", "")
            
            metadata = {
                "finish_reason": candidate.get("finishReason"),
                "token_usage": data.get("usageMetadata"),
                "raw_provider_metadata": data,
            }
            
            return LLMResponse(
                content=content,
                model=model,
                provider="gemini",
                metadata=metadata
            )
        except (KeyError, IndexError, TypeError) as e:
            raise LLMResponseParseError(f"Failed to parse Gemini response: {e}") from e
