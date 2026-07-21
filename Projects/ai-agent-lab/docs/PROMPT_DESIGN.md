# Prompt Design

## Purpose
The Prompt Framework provides a standardized, modular way to manage and render LLM prompts, ensuring separation of concerns between agents and prompt engineering.

## Architecture
- `PromptTemplate`: Immutable definition of a prompt.
- `PromptVariables`: Strongly typed container for prompt variables.
- `PromptRenderer`: Responsible for deterministic template rendering.
- `PromptRegistry`: Centralized storage and discovery for templates.
- `PromptBuilder` (Interface) / `DefaultPromptBuilder`: Facade for agents to request rendered prompts.

## Components
- `PromptTemplate`: Stores name, version, and template string.
- `PromptVariables`: Validates and holds data for substitution.
- `PromptRenderer`: Handles variable substitution (using standard python formatting).
- `PromptRegistry`: Manages registration and retrieval of templates.
- `PromptBuilder`: The interface agents interact with to get final prompt text.

## Lifecycle
1. Registration: Templates are registered in `PromptRegistry` (via bootstrap).
2. Request: Agent calls `PromptBuilder` with template ID and variables.
3. Lookup: `PromptBuilder` gets `PromptTemplate` from `PromptRegistry`.
4. Render: `PromptBuilder` uses `PromptRenderer` to substitute variables.
5. Delivery: Final string returned to Agent.

## Template Management
- **Registration**: All templates must be registered in the `PromptRegistry` during system bootstrap.
- **Versioning**: Each template has a `version` string. This allows for A/B testing and incremental updates to prompt engineering without breaking existing agents.
- **Backward Compatibility**: When updating a template, create a new version if changes are not strictly backward-compatible. Agents requiring specific behavior should request specific versions if supported.
- **Template Evolution**: Templates are expected to evolve. Agents should use the registry to obtain the latest version unless otherwise specified.

## Future Evolution: External Templates
While currently managed within Python code, the framework is designed to support future evolution toward externally stored prompt templates (e.g., Markdown files, YAML, or JSON configurations). This would involve:
1. Extending `PromptRegistry` to load templates from a configured directory or database.
2. Introducing a `TemplateLoader` service for deserializing external formats.
3. Keeping `PromptBuilder` and `PromptRenderer` interfaces unchanged to ensure no disruption to agents.

## Design Principles
- Separation of Concerns: Prompt strings are kept out of agent code.
- Determinism: Rendering must produce predictable results given the same input.
- Type Safety: Prompt variables are validated.
- Modularity: Templates are stored as independent units.

