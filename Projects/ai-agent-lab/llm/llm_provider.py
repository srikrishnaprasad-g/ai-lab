'''Abstract base class for LLM providers.
'''

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    '''
    Abstract base class for LLM providers.

    This class defines the interface that all LLM provider implementations must adhere to.
    It includes abstract methods for generating text, specifying the provider name,
    and specifying the model name.
    '''

    @abstractmethod
    def generate(self, prompt: str) -> str:
        '''Generates text based on the given prompt.

        Args:
            prompt: The input prompt for text generation.

        Returns:
            The generated text.
        '''
        pass

    @abstractmethod
    def provider_name(self) -> str:
        '''Returns the name of the LLM provider.

        Returns:
            The name of the provider (e.g., "openai", "anthropic").
        '''
        pass

    @abstractmethod
    def model_name(self) -> str:
        '''Returns the name of the model being used.

        Returns:
            The name of the model (e.g., "gpt-4", "claude-3-opus").
        '''
        pass


