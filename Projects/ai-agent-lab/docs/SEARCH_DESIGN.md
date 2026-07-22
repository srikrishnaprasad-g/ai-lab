# Search Design

## Purpose
The Search Framework provides a production-ready, provider-agnostic interface for performing web searches. It decouples the `SearchTool` from specific search engine implementations, allowing for easy provider swaps and reliable testing.

## Architecture
- `SearchProvider` (ABC): Abstract interface that defines the search contract.
- `DuckDuckGoProvider`: Production implementation of the `SearchProvider` using `HttpClient`.
- `SearchService`: Wrapper service used by tools to interact with providers, providing a cleaner API.
- `SearchResult` / `SearchResponse`: Standardized data models for search results and responses.

## Components
- `SearchProvider` (ABC): Defines the `search()` method.
- `DuckDuckGoProvider`: Implements `SearchProvider` for the DuckDuckGo Instant Answer API.
- `SearchService`: Provides a high-level `perform_search` method.
- `HttpClient`: Used by providers to execute authenticated or authorized network requests.

## Provider Lifecycle
1. Initialization: `SearchProvider` is instantiated with `HttpClient` and `SearchProviderConfig` via `RuntimeBootstrap`.
2. Execution: The `SearchService` delegates the `search()` call to the configured provider.
3. Response Processing: Provider maps raw API data to `SearchResponse`.

## Design Principles
- **Provider Abstraction**: Tools depend on `SearchProvider`, not concrete providers.
- **Dependency Injection**: Providers and clients are injected at the composition root.
- **Determinism (Testing)**: All tests must use `MockSearchProvider` or mock the `HttpClient` to ensure no network access during testing.
- **Resilience**: Providers must translate HTTP exceptions into domain-specific exceptions (e.g., `SearchProviderError`).
- **Extensibility**: Adding new providers involves only creating a new implementation of `SearchProvider`.
