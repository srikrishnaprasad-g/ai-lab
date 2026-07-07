'''Groq LLM provider implementation.
'''

from llm.llm_provider import LLMProvider


class GroqProvider(LLMProvider):
    """
    Implementation of the LLMProvider for the Groq API.

    This class provides the basic structure for interacting with the Groq LLM.
    The actual API calls are deferred to a future sprint.

    Attributes:
        api_key: The API key for authenticating with the Groq API.
        model: The name of the Groq model to use.
    """

    def __init__(self, api_key: str, model: str) -> None:
        """Initializes the GroqProvider.

        Args:
            api_key: The API key for the Groq API.
            model: The name of the Groq model to use.
        """
        self._api_key = api_key
        self._model = model

    def generate(self, prompt: str) -> str:
        """Generates text based on the given prompt using the Groq API.

        Args:
            prompt: The input prompt for text generation.

        Returns:
            The generated text.

        Raises:
            NotImplementedError: Indicates that the Groq API integration is
                                 planned for a future sprint.
        """
        # TODO: Implement Groq API integration for text generation.
        raise NotImplementedError(
            "Groq API integration will be implemented in Sprint 2."
        )

    def provider_name(self) -> str:
        """Returns the name of the LLM provider.

        Returns:
            The name of the provider, which is "groq".
        """
        return "groq"

    def model_name(self) -> str:
        """Returns the name of the Groq model being used.

        Returns:
            The name of the model.
        """
        return self._model
