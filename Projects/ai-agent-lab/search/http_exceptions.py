"""Generic HTTP client exceptions."""

class HTTPClientError(Exception):
    """Base exception for all HTTP client errors."""
    pass


class HTTPTimeoutError(HTTPClientError):
    """Raised when request times out."""
    pass


class HTTPRequestError(HTTPClientError):
    """Raised when a general HTTP error occurs."""
    def __init__(self, message: str, status_code: int | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
