"""HTTP client abstraction."""

from typing import Any
import httpx
from search.http_exceptions import HTTPTimeoutError, HTTPRequestError

class HttpClient:
    """Wrapper around a persistent httpx.Client for GET/POST requests."""

    def __init__(self, timeout: float = 10.0) -> None:
        self._client = httpx.Client(timeout=timeout)

    def get(self, url: str, params: dict[str, Any] | None = None) -> Any:
        """Performs a GET request."""
        try:
            response = self._client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException as e:
            raise HTTPTimeoutError(f"Request timed out: {e}") from e
        except httpx.HTTPError as e:
            raise HTTPRequestError(f"HTTP error occurred: {e}") from e

    def post(self, url: str, json: dict[str, Any] | None = None) -> Any:
        """Performs a POST request."""
        try:
            response = self._client.post(url, json=json)
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException as e:
            raise HTTPTimeoutError(f"Request timed out: {e}") from e
        except httpx.HTTPError as e:
            raise HTTPRequestError(f"HTTP error occurred: {e}") from e

    def close(self) -> None:
        """Closes the client."""
        self._client.close()
