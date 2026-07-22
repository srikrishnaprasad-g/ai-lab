"""Search provider factory."""

from typing import Type

from config.settings import Settings
from search.exceptions import UnsupportedSearchProviderError
from search.providers.tavily_provider import TavilyProvider
from search.search_provider import SearchProvider
from search.search_provider_config import SearchProviderConfig
from search.http_client import HttpClient


class SearchProviderFactory:
    """Factory for creating search provider instances."""

    _PROVIDER_REGISTRY: dict[str, Type[SearchProvider]] = {
        "tavily": TavilyProvider,
    }

    def __init__(self, settings: Settings) -> None:
        """Initializes the factory with settings."""
        self._settings = settings

    def create_provider(self, provider_name: str | None = None) -> SearchProvider:
        """Creates a search provider instance."""
        if provider_name is None:
            provider_name = self._settings.default_search_provider

        provider_cls = self._PROVIDER_REGISTRY.get(provider_name)
        if provider_cls:
            # Create config and http client for the provider
            config = SearchProviderConfig(
                max_results=self._settings.default_search_max_results,
                timeout=self._settings.default_search_timeout,
            )
            http_client = HttpClient(timeout=config.timeout)
            
            # Tavily requires an API key
            if provider_name == "tavily":
                return provider_cls(http_client, config, api_key=self._settings.tavily_api_key)
            
            return provider_cls(http_client, config)
        raise UnsupportedSearchProviderError(f"Unsupported provider: {provider_name}")

