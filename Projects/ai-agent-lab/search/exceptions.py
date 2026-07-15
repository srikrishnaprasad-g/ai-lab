"""Search-specific exception definitions."""


class SearchException(Exception):
    """Base exception for all search-related errors."""
    pass


class SearchProviderError(SearchException):
    """General error from the search provider."""
    pass


class SearchAuthenticationError(SearchException):
    """Raised when authentication fails."""
    pass


class SearchRateLimitError(SearchException):
    """Raised when rate limits are exceeded."""
    pass


class SearchTimeoutError(SearchException):
    """Raised when request times out."""
    pass


class SearchResponseParseError(SearchException):
    """Raised when response cannot be parsed."""
    pass


class UnsupportedSearchProviderError(SearchException):
    """Raised when an unsupported search provider is requested."""
    pass
