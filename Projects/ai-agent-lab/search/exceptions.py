"""Search-specific exception definitions."""


class SearchException(Exception):
    """Base exception for all search-related errors."""
    pass


class UnsupportedSearchProviderError(SearchException):
    """Raised when an unsupported search provider is requested."""
    pass
