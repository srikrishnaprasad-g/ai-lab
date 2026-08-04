from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "Executive Research"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    REPORTS_DIR: str = "reports"

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

settings = Settings()
