"""Gemini provider implementation."""

import logging
from observability.log_utils import mask_api_key

from llm.exceptions import (
    LLMException, 
    LLMAuthenticationError, 
    LLMRateLimitError, 
    LLMTimeoutError, 
    LLMProviderError
)
from llm.llm_provider import BaseLLMProvider
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse
from llm.providers.gemini_response_mapper import GeminiResponseMapper
from search.http_exceptions import HTTPTimeoutError, HTTPRequestError

logger = logging.getLogger("pipeline")


class GeminiProvider(BaseLLMProvider):
    """Production implementation for Gemini."""

    def provider_name(self) -> str:
        return "gemini"

    def generate(self, request: LLMRequest) -> LLMResponse:
        # TODO: Implement streaming support here in Sprint 5
        
        model = request.model or self._config.model
        if not model:
           raise LLMException(
              "No Gemini model configured. Set DEFAULT_LLM_MODEL or provide request.model."
        )
        api_version = self._config.api_version or "v1"
        base_url = self._config.base_url or "https://generativelanguage.googleapis.com"
        
        url = f"{base_url}/{api_version}/models/{model}:generateContent"

        
        payload = {
            "contents": [{"parts": [{"text": request.prompt}]}],
        }
        
        if request.system_prompt:
            payload["systemInstruction"] = {"parts": [{"text": request.system_prompt}]}
        
        if request.temperature is not None:
            payload.setdefault("generationConfig", {})["temperature"] = request.temperature
        if request.max_tokens is not None:
            payload.setdefault("generationConfig", {})["maxOutputTokens"] = request.max_tokens
        
        try:
            # Construct URL with key parameter
            masked_key = mask_api_key(self._config.api_key)
            final_url = f"{url}?key={self._config.api_key}"
            # Log the request URL using the masked key for safety if the client logs it
            masked_url = f"{url}?key={masked_key}"
            logger.debug(f"Request URL: {masked_url}")
            
            response_data = self._http_client.post(final_url, json=payload)
            return GeminiResponseMapper.map_response(response_data, model)
        except HTTPTimeoutError as e:
            raise LLMTimeoutError(f"Gemini request timed out: {e}") from e
        except HTTPRequestError as e:
            if e.status_code in [401, 403]:
                raise LLMAuthenticationError(f"Authentication failed: {e}") from e
            elif e.status_code == 429:
                raise LLMRateLimitError(f"Rate limit exceeded: {e}") from e
            elif e.status_code and 500 <= e.status_code < 600:
                raise LLMProviderError(f"Gemini server error: {e}") from e
            else:
                raise LLMProviderError(f"Gemini API request failed: {e}") from e
        except Exception as e:
            raise LLMException(f"Unexpected Gemini error: {e}") from e
