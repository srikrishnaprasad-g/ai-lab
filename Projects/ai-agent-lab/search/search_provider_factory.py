"""Search provider factory."""

from typing import Type

from config.settings import Settings
from search.exceptions import UnsupportedSearchProviderError
from search.providers.duckduckgo_provider import DuckDuckGoProvider
from search.search_provider import SearchProvider


class SearchProviderFactory:
    """Factory for creating search provider instances."""

    _PROVIDER_REGISTRY: dict[str, Type[SearchProvider]] = {
        "duckduckgo": DuckDuckGoProvider,
    }

    def __init__(self, settings: Settings) -> None:
        """Initializes the factory with settings.

        Args:
            settings: The application settings.
        """
        self._settings = settings

    def create_provider(self, provider_name: str | None = None) -> SearchProvider:
        """Creates a search provider instance.

        Args:
            provider_name: The name of the provider. If None, uses settings.

        Returns:
            An instantiated SearchProvider.

        Raises:
            UnsupportedSearchProviderError: If the provider is unknown.
        """
        if provider_name is None:
            provider_name = self._settings.default_search_provider

        provider_cls = self._PROVIDER_REGISTRY.get(provider_name)

        if provider_cls:
            return provider_cls()

        raise UnsupportedSearchProviderError(f"Unsupported provider: {provider_name}")
