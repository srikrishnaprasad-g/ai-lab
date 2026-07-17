'''Configuration module.
'''

import os
import typing
import types
from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from dotenv import load_dotenv


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
        log_level: The logging level for the application.
        default_search_provider: The default search provider.
        default_search_max_results: The max search results limit.
        default_search_timeout: The search provider timeout.
        default_llm_provider: The default LLM provider.
        default_llm_model: The default LLM model.
        default_llm_timeout: The default LLM timeout.
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
    default_search_timeout: float = field(
        default=10.0,
        metadata={"env_var": "DEFAULT_SEARCH_TIMEOUT"},
    )
    default_llm_provider: str = field(
        default="mock",
        metadata={"env_var": "DEFAULT_LLM_PROVIDER"},
    )
    default_llm_model: str = field(
        default="mock-model",
        metadata={"env_var": "DEFAULT_LLM_MODEL"},
    )
    default_llm_timeout: float = field(
        default=30.0,
        metadata={"env_var": "DEFAULT_LLM_TIMEOUT"},
    )

    def __post_init__(self):
        """Post-initialization validation and environment variable loading."""
        for field_name, field_info in self.__dataclass_fields__.items():
            env_var = field_info.metadata.get("env_var")
            if env_var:
                value = os.getenv(env_var)
                if value is not None:
                    try:
                        converted_value = self._convert_value(value, field_info.type)
                        setattr(self, field_name, converted_value)
                    except (ValueError, TypeError):
                        # Keep default if conversion fails
                        pass

    def _convert_value(self, value: str, field_type: Any) -> Any:
        """Converts string value to the appropriate type."""
        # Handle Union (Optional) - PEP 604 and typing.Union
        origin = typing.get_origin(field_type)
        if origin in (typing.Union, types.UnionType):
            args = typing.get_args(field_type)
            for arg in args:
                if arg is type(None):  # noqa: E721
                    continue
                try:
                    return self._convert_value(value, arg)
                except (ValueError, TypeError):
                    continue
            raise ValueError(f"Could not convert {value} to {field_type}")

        # Handle Enum
        if isinstance(field_type, type) and issubclass(field_type, Enum):
            return field_type(value.upper())

        # Handle Bool
        if field_type is bool:
            normalized = value.lower()
            if normalized in ('true', '1', 'yes'):
                return True
            if normalized in ('false', '0', 'no'):
                return False
            raise ValueError(f"Invalid boolean value: {value}")

        # Default to constructor
        return field_type(value)

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


from pathlib import Path
from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_ENV_FILE = _PROJECT_ROOT / ".env"

def load_settings() -> Settings:
    """Loads the application settings."""    
    load_dotenv(dotenv_path=_ENV_FILE, override=True)
    return Settings()
