"""Search provider abstraction."""

from abc import ABC, abstractmethod
from search.search_response import SearchResponse


class SearchProvider(ABC):
    """Abstract base class defining the contract for all search providers."""

    @abstractmethod
    def search(self, query: str, max_results: int) -> SearchResponse:
        """Executes a search query."""
        pass

    @abstractmethod
    def provider_name(self) -> str:
        """Returns the name of the provider."""
        pass
