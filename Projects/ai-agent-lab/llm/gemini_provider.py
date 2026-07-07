'''Gemini LLM provider implementation.
'''

from llm.llm_provider import LLMProvider


class GeminiProvider(LLMProvider):
    """
    Implementation of the LLMProvider for the Gemini API.

    This class provides the basic structure for interacting with the Gemini LLM.
    The actual API calls are deferred to a future sprint.

    Attributes:
        api_key: The API key for authenticating with the Gemini API.
        model: The name of the Gemini model to use.
    """

    def __init__(self, api_key: str, model: str) -> None:
        """Initializes the GeminiProvider.

        Args:
            api_key: The API key for the Gemini API.
            model: The name of the Gemini model to use.
        """
        self._api_key = api_key
        self._model = model

    def generate(self, prompt: str) -> str:
        """Generates text based on the given prompt using the Gemini API.

        Args:
            prompt: The input prompt for text generation.

        Returns:
            The generated text.

        Raises:
            NotImplementedError: Indicates that the Gemini API integration is
                                 planned for a future sprint.
        """
        # TODO: Implement Gemini API integration for text generation.
        raise NotImplementedError(
            "Gemini API integration will be implemented in Sprint 2."
        )

    def provider_name(self) -> str:
        """Returns the name of the LLM provider.

        Returns:
            The name of the provider, which is "gemini".
        """
        return "gemini"

    def model_name(self) -> str:
        """Returns the name of the Gemini model being used.

        Returns:
            The name of the model.
        """
        return self._model
