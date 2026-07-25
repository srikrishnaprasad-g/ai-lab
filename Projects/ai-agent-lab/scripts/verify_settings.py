from config.settings import load_settings

settings = load_settings()
print(f"Gemini API key ends with 92OQ: {settings.gemini_api_key.endswith('92OQ')}")
print(f"Default LLM model: {settings.default_llm_model}")
assert settings.gemini_api_key.endswith('92OQ')
assert settings.default_llm_model == "gemini-3.1-flash-lite"
