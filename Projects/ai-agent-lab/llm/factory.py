'''Provider factory module.
'''

from llm.llm_provider import LLMProvider
from config.settings import Settings


from llm.gemini_provider import GeminiProvider
from llm.groq_provider import GroqProvider


class LLMProviderFactory:
    """
    Factory class for creating LLMProvider instances.

    This factory is responsible for instantiating the correct LLM provider
    based on the application settings.
    """

    def __init__(self, settings: Settings) -> None:
        """Initializes the ProviderFactory with application settings.

        Args:
            settings: The application settings object.
        """
        self.settings = settings

    def create_provider(self) -> LLMProvider:
        """Creates and returns an LLMProvider instance based on the default configuration.

        Raises:
            ValueError: If the configured default provider is unsupported.

        Returns:
            An instance of an LLMProvider.
        """
        provider_name = self.settings.default_provider.strip().lower()

        if provider_name == "gemini":
            return GeminiProvider(api_key=self.settings.get_gemini_api_key(), model=self.settings.default_model)
        elif provider_name == "groq":
            return GroqProvider(api_key=self.settings.get_groq_api_key(), model=self.settings.default_model)
        # TODO: Add registration for new providers here
        # elif provider_name == "openai":
        #     return OpenAIProvider(settings=self.settings)
        else:
            raise ValueError(f"Unsupported LLM provider: {provider_name}")

