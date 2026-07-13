"""LLM-specific exception definitions."""


class LLMException(Exception):
    """Base exception for all LLM-related errors."""
    pass


class UnsupportedLLMProviderError(LLMException):
    """Raised when an unsupported LLM provider is requested."""
    pass
