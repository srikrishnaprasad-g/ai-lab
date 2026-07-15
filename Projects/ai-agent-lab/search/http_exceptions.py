"""Generic HTTP client exceptions."""

class HTTPClientError(Exception):
    """Base exception for all HTTP client errors."""
    pass


class HTTPTimeoutError(HTTPClientError):
    """Raised when request times out."""
    pass


class HTTPRequestError(HTTPClientError):
    """Raised when a general HTTP error occurs."""
    pass
