# Extension Guide

## Adding Providers
1. Define abstract interface in the corresponding package (`llm/`, `search/`).
2. Implement the concrete provider.
3. Add to the corresponding Factory (e.g., `LLMProviderFactory`).
4. Update configuration to support the new provider.

## Adding Tools
1. Inherit from `Tool`.
2. Implement `execute`.
3. Register the tool in `ToolRegistry`.
