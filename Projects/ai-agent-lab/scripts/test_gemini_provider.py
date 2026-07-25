"""Test script for GeminiProvider."""

import sys
from config.settings import load_settings
from llm.llm_provider_factory import LLMProviderFactory
from llm.llm_request import LLMRequest

def test_gemini_provider() -> None:
    """Tests the GeminiProvider by sending a simple prompt."""
    print("Testing GeminiProvider...")
    
    settings = load_settings()
    factory = LLMProviderFactory(settings)
    
    try:
        provider = factory.create_provider(provider_name="gemini")
        print(f"Provider: {provider.provider_name()}")
        
        request = LLMRequest(prompt="Say hello in one sentence.")
        response = provider.generate(request)
        
        print(f"Model: {response.model}")
        print(f"Generated Response: {response.content}")
        print(f"Metadata: {response.metadata}")
        
        print("GeminiProvider test passed successfully!")
    except Exception as e:
        print(f"GeminiProvider test failed: {e}")
        raise

if __name__ == "__main__":
    try:
        test_gemini_provider()
        sys.exit(0)
    except Exception:
        sys.exit(1)
