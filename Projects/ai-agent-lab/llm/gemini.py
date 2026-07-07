import os
import logging
from typing import Optional

import google.generativeai as genai
from .base import LLMProvider

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GeminiClient(LLMProvider):
    \"\"\"
    A concrete implementation of LLMProvider for interacting with Google's Gemini LLM.

    This client uses the Google GenAI Python SDK to communicate with Gemini models.
    It handles API key and model name configuration via environment variables
    and provides structured logging and exception handling.
    \"\"\"

    def __init__(self):
        \"\"\"
        Initializes the GeminiClient, configuring the Google GenAI SDK.

        Raises:
            ValueError: If GOOGLE_API_KEY or GEMINI_MODEL_NAME environment variables are not set.
        \"\"\"
        self.api_key: Optional[str] = os.getenv("GOOGLE_API_KEY")
        self.model_name: Optional[str] = os.getenv("GEMINI_MODEL_NAME")

        if not self.api_key:
            logger.error("GOOGLE_API_KEY environment variable not set.")
            raise ValueError("GOOGLE_API_KEY environment variable not set.")
        if not self.model_name:
            logger.error("GEMINI_MODEL_NAME environment variable not set.")
            raise ValueError("GEMINI_MODEL_NAME environment variable not set.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)
        logger.info(f"GeminiClient initialized with model: {self.model_name}")

    def generate(self, prompt: str) -> str:
        \"\"\"\
        Generates a text response from the configured Gemini model.

        Args:
            prompt: The input prompt string for the LLM.

        Returns:
            The generated text as a string.

        Raises:
            Exception: If an error occurs during the API call to the Gemini model.
        \"\"\"
        try:
            logger.info(f"Generating response for prompt (first 50 chars): {prompt[:50]}...")
            response = self.model.generate_content(prompt)
            generated_text = response.text
            logger.info(f"Successfully generated response (first 50 chars): {generated_text[:50]}...")
            return generated_text
        except Exception as e:
            logger.error(f"Error generating content with Gemini model: {e}", exc_info=True)
            raise Exception(f"Failed to generate content with Gemini: {e}")
