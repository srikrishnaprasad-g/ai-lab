'''Configuration module.
'''

import os
from dataclasses import dataclass, field
from enum import Enum


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class Settings:
    """Application settings.

    Reads configuration from environment variables with sensible defaults.

    Attributes:
        gemini_api_key: The API key for the Gemini provider.
        groq_api_key: The API key for the Groq provider.
        default_provider: The default LLM provider to use.
        default_model: The default LLM model to use.
        log_level: The logging level for the application.
    """

    gemini_api_key: str | None = field(
        default=None,
        metadata={"env_var": "GEMINI_API_KEY"},
        repr=False  # Avoid printing API keys
    )
    groq_api_key: str | None = field(
        default=None,
        metadata={"env_var": "GROQ_API_KEY"},
        repr=False  # Avoid printing API keys
    )
    default_provider: str = field(
        default="gemini",
        metadata={"env_var": "DEFAULT_PROVIDER"},
    )
    default_model: str = field(
        default="gemini-2.5-flash",
        metadata={"env_var": "DEFAULT_MODEL"},
    )
    log_level: LogLevel = field(
        default=LogLevel.INFO,
        metadata={"env_var": "LOG_LEVEL"},
    )
    default_search_provider: str = field(
        default="duckduckgo",
        metadata={"env_var": "DEFAULT_SEARCH_PROVIDER"},
    )
    default_search_max_results: int = field(
        default=3,
        metadata={"env_var": "DEFAULT_SEARCH_MAX_RESULTS"},
    )
    default_llm_provider: str = field(
        default="mock",
        metadata={"env_var": "DEFAULT_LLM_PROVIDER"},
    )
    default_llm_model: str = field(
        default="mock-model",
        metadata={"env_var": "DEFAULT_LLM_MODEL"},
    )

    def __post_init__(self):
        """Post-initialization validation and environment variable loading."""
        for field_info in self.__dataclass_fields__.values():
            env_var = field_info.metadata.get("env_var")
            if env_var:
                value = os.getenv(env_var)
                if value is not None:
                    # Convert environment variable to the field's type
                    if field_info.type == LogLevel:
                        try:
                            setattr(self, field_info.name, LogLevel(value.upper()))
                        except ValueError:
                            # Keep default if env var is invalid
                            pass
                    else:
                        try:
                            setattr(self, field_info.name, field_info.type(value))
                        except (ValueError, TypeError):
                            # Keep default if env var is invalid
                            pass

    def get_gemini_api_key(self) -> str:
        """Gets the Gemini API key, raising an error if not set."""
        if not self.gemini_api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")
        return self.gemini_api_key

    def get_groq_api_key(self) -> str:
        """Gets the Groq API key, raising an error if not set."""
        if not self.groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable not set.")
        return self.groq_api_key


def load_settings() -> Settings:
    """Loads the application settings."""
    return Settings()
