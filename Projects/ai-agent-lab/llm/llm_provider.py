"""LLM provider abstraction."""

from abc import ABC, abstractmethod
from llm.llm_request import LLMRequest
from llm.llm_response import LLMResponse
from llm.llm_provider_config import LLMProviderConfig
# TODO: Move HttpClient to shared infrastructure (e.g., infra/ or common/) 
# to decouple LLM framework from Search framework.
from search.http_client import HttpClient


class LLMProvider(ABC):
    """Abstract base class defining the contract for all LLM providers."""

    @abstractmethod
    def generate(self, request: LLMRequest) -> LLMResponse:
        """Generates a response from the LLM."""
        pass

    @abstractmethod
    def provider_name(self) -> str:
        """Returns the name of the provider."""
        pass


class BaseLLMProvider(LLMProvider):
    """Base class for infrastructure-shared LLM provider functionality."""

    def __init__(self, http_client: HttpClient, config: LLMProviderConfig) -> None:
        """Initializes the base provider with shared infrastructure.

        Args:
            http_client: The HTTP client for network communication.
            config: Provider-specific infrastructure configuration.
        """
        self._http_client = http_client
        self._config = config
