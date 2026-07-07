import abc

class LLMProvider(abc.ABC):
    """
    Abstract Base Class for LLM providers.

    This class defines the interface that all LLM providers must implement.
    It ensures that different LLM services can be used interchangeably by the agent code.
    """

    @abc.abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates a response from the LLM based on the given prompt.

        Args:
            prompt: The input prompt for the LLM.

        Returns:
            The generated text response from the LLM.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def provider_name(self) -> str:
        """
        Returns the name of the LLM provider.

        Returns:
            A string representing the name of the LLM provider (e.g., "Gemini", "OpenAI", "Groq").
        """
        raise NotImplementedError

    @abc.abstractmethod
    def model_name(self) -> str:
        """
        Returns the name of the specific model being used by the provider.

        Returns:
            A string representing the name of the LLM model (e.g., "gemini-pro", "gpt-4", "llama3-8b-8192").
        """
        raise NotImplementedError
