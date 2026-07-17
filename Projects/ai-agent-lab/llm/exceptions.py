"""LLM-specific exception definitions."""


class LLMException(Exception):
    """Base exception for all LLM-related errors."""
    pass


class LLMProviderError(LLMException):
    """General error from the LLM provider."""
    pass


class LLMAuthenticationError(LLMException):
    """Raised when authentication fails."""
    pass


class LLMRateLimitError(LLMException):
    """Raised when rate limits are exceeded."""
    pass


class LLMTimeoutError(LLMException):
    """Raised when request times out."""
    pass


class LLMResponseParseError(LLMException):
    """Raised when response cannot be parsed."""
    pass


class UnsupportedLLMProviderError(LLMException):
    """Raised when an unsupported LLM provider is requested."""
    pass
