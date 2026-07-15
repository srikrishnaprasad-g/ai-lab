"""Search provider configuration."""

from dataclasses import dataclass


@dataclass
class SearchProviderConfig:
    """Configuration for search providers."""

    api_key: str | None = None
    timeout: float = 10.0
    safe_search: bool = True
    max_results: int = 3
