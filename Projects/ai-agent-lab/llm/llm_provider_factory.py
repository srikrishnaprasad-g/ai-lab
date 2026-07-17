"""LLM provider factory."""

from typing import Type
from config.settings import Settings
from llm.exceptions import UnsupportedLLMProviderError
from llm.llm_provider import LLMProvider
from llm.llm_provider_config import LLMProviderConfig
from llm.providers.mock_provider import MockLLMProvider
from llm.providers.gemini_provider import GeminiProvider
from llm.providers.groq_provider import GroqProvider
from llm.providers.openrouter_provider import OpenRouterProvider
from search.http_client import HttpClient


class LLMProviderFactory:
    """Factory for creating LLM provider instances."""

    _PROVIDER_REGISTRY: dict[str, Type[LLMProvider]] = {
        "mock": MockLLMProvider,
        "gemini": GeminiProvider,
        "groq": GroqProvider,
        "openrouter": OpenRouterProvider,
    }

    def __init__(self, settings: Settings) -> None:
        """Initializes the factory with settings."""
        self._settings = settings

    def create_provider(self, provider_name: str | None = None) -> LLMProvider:
        """Creates an LLM provider instance."""
        if provider_name is None:
            provider_name = self._settings.default_llm_provider

        provider_cls = self._PROVIDER_REGISTRY.get(provider_name)
        if provider_cls:
            # Resolve API key based on provider
            api_key = None
            if provider_name == "gemini":
                api_key = self._settings.get_gemini_api_key()
            elif provider_name == "groq":
                api_key = self._settings.get_groq_api_key()
                
            # Create config and http client for the provider
            config = LLMProviderConfig(
                timeout=self._settings.default_llm_timeout,
                model=self._settings.default_llm_model,
                api_key=api_key
            )
            http_client = HttpClient(timeout=config.timeout)
            
            return provider_cls(http_client, config)

        raise UnsupportedLLMProviderError(f"Unsupported provider: {provider_name}")
