# Prompt Design

## Purpose
The Prompt Framework provides a standardized, modular way to manage and render LLM prompts, ensuring separation of concerns between agents and prompt engineering.

## Architecture
- `PromptTemplate`: Immutable definition of a prompt.
- `PromptVariables`: Strongly typed container for prompt variables.
- `PromptRenderer`: Responsible for deterministic template rendering.
- `PromptRegistry`: Centralized storage and discovery for templates.
- `PromptBuilder`: The interface agents interact with to get final prompt text.

## Components
- `PromptTemplate`: Stores name, version, and template string.
- `PromptVariables`: Validates and holds data for substitution.
- `PromptRenderer`: Handles variable substitution.
- `PromptRegistry`: Manages registration and retrieval of templates.
- `SummaryPromptBuilder`: Implements `PromptBuilder` for the Summary Agent.

## Lifecycle
1. Registration: Templates are registered in `PromptRegistry` (via `RuntimeBootstrap`).
2. Request: Agent calls `PromptBuilder` with template ID and variables.
3. Lookup: `PromptBuilder` gets `PromptTemplate` from `PromptRegistry`.
4. Render: `PromptBuilder` uses `PromptRenderer` to substitute variables.
5. Delivery: Final string returned to Agent.

## Template Management
- **Registration**: All templates must be registered in the `PromptRegistry` during system bootstrap.
- **Versioning**: Each template has a `version` string.
- **Backward Compatibility**: When updating a template, create a new version.
- **Template Evolution**: Templates are currently defined in `prompts/templates.py`. Future evolution will support external template files.

## Summary Agent Prompts
The Summary Agent uses a two-part prompt approach:
- System: Defines role, constraints, and conflict resolution policies.
- User: Binds the search results and query context.

These are defined in `prompts/templates.py` and managed via `SummaryPromptBuilder`.

## Design Principles
- Separation of Concerns: Prompt strings are kept out of agent code.
- Determinism: Rendering must produce predictable results.
- Type Safety: Prompt variables are validated.
- Modularity: Templates are stored as independent units.

