"""Logging utilities."""

def mask_api_key(key: str) -> str:
    """Masks API keys, preserving first and last 4 characters."""
    if not key or len(key) <= 8:
        return "****"
    return f"{key[:4]}{'*' * (len(key) - 8)}{key[-4:]}"
