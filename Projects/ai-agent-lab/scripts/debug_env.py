import os
from dotenv import load_dotenv
load_dotenv()
print(f"ENV: {os.getenv('GEMINI_API_KEY')}")
from config.settings import load_settings
settings = load_settings()
print(f"Settings: {settings.gemini_api_key}")
