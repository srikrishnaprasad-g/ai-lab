"""LLM provider configuration."""

from dataclasses import dataclass


@dataclass
class LLMProviderConfig:
    """Infrastructure configuration for LLM providers."""

    api_key: str | None = None
    base_url: str | None = None
    timeout: float = 30.0
