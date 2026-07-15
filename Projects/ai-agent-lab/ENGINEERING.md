This document will define the engineering practices for the AI Agent Lab project.

# Architecture First Principle

- Design before implementation.
- Major components should be reviewed before code generation.

# Engineering Principles

- Build incrementally.
- One task at a time.
- Keep changes small.
- Prioritize readability over cleverness.
- Production-quality code only.

# Development Workflow

For every task:

1. Understand the requirement.
2. Review PROJECT.md.
3. Implement only the requested scope.
4. Keep changes localized.
5. Review your own implementation.
6. Run tests.
7. Runtime validation is mandatory.
8. Compilation alone is insufficient.
9. Prepare for commit.
10. Prefer extending interfaces over changing existing public APIs.

# AI-Assisted Development Workflow

Roles:

- ChatGPT: Staff Engineer / Architect
- Claude Code: Software Engineer
- User: Product Owner / Engineering Manager

Claude Code/Gemini CLI should:
- implement code
- explain design decisions
- perform self-review
- avoid making unrelated changes

# Task Size Rules

Each task should generally modify:

- one class
- one file
- one responsibility

Avoid large refactors unless explicitly requested.

# Code Review Checklist

Before considering a task complete, verify:

- Type hints exist.
- Public methods have docstrings.
- Naming is clear.
- Error handling is appropriate.
- Logging is used instead of print().
- No duplicated logic.
- No dead code.

# Git Workflow

One logical task = one commit.

Commit messages should follow:

- Add ...
- Implement ...
- Refactor ...
- Fix ...
- Update ...

Keep commits focused.

# Definition of Done

A task is complete only if:

- Requirements are satisfied.
- Code is readable.
- No unnecessary complexity.
- Self-review completed.
- Ready to commit.

Every implementation must satisfy all of the following before commit:

- Architecture reviewed
- Claude/Gemini CLI self-review completed
- Code compiles (`python -m py_compile`)
- Imports validated
- No TODOs blocking current sprint
- Git commit created with meaningful message

# Verification Suite Convention

Every major component gets a smoke test.

scripts/
│
├── test_groq.py
├── test_gemini.py
├── test_factory.py
├── test_tool_registry.py
└── test_orchestrator.py

Framework components should be validated using reusable smoke test scripts rather than manual REPL sessions whenever practical.

This is different from pytest.

These are executable developer diagnostics.

### Runtime Validation Rule

After every change to a dataclass, package API, or runtime contract:

1. Exit any running Python REPL.
2. Start a fresh Python interpreter.
3. Re-run import and runtime validation.

Do not rely on an existing REPL session after modifying source files.

# Regression Suite Convention

Example Requests

examples/

research_ai.txt

research_quantum.txt

research_llms.txt

Whenever we finish a sprint, we rerun these.

If they still work...

We know we didn't break anything.

This becomes our regression suite

# Prompting Guidelines

Every implementation prompt should begin with:

"Read PROJECT.md and ENGINEERING.md before making changes."

Prompts should request only one logical task.

# Documentation Rules

Whenever architecture changes:

- Update PROJECT.md.
- Update ENGINEERING.md if engineering practices change.
- Update README.md if setup changes.

Write the document in professional Markdown suitable for an open-source project.

Do not modify any other files.

## Repository Hygiene

Before every commit:

- Review git status.
- Remove generated artifacts from version control.
- Never commit __pycache__, logs, temporary files, or IDE metadata.
- Prefer small, logically grouped commits over large mixed commits.

## Agent Design Rule

Agents must never directly instantiate Tools.

All Tool access must occur through ToolRegistry using dependency injection.

This preserves loose coupling, enables tool replacement, and improves testability.

## Integration Validation Rule

Whenever a new Agent or Tool is introduced:

1. Register it through the appropriate Registry.
2. Validate it through the RuntimeOrchestrator.
3. Do not validate components in isolation if they are intended to participate in the runtime workflow.

##Validation Policy

Every commit must satisfy:

1. py_compile succeeds

2. Runtime smoke test passes

python scripts/test_runtime_workflow.py

3. Architecture review completed

4. No broken imports

5. Git status clean before commit

## Provider Architecture

- External services (LLMs, Search, OCR, Storage, etc.) must always be accessed through provider abstractions.
- Components (Agents, Tools, Runtime) must depend on provider interfaces rather than concrete implementations.
- Configuration must be resolved during RuntimeBootstrap and injected into components via constructors. Components must never read application settings directly.
- RuntimeBootstrap is the only composition root.
- Factories and Settings must only be used inside RuntimeBootstrap.
- Agents and Tools depend only on abstract provider interfaces.
- Configuration is injected through constructors.
- Providers are never instantiated directly inside business logic.

## Prompt Builder Principles

- Prompt construction belongs exclusively to PromptBuilder implementations.
- Agents orchestrate workflows.
- PromptBuilders transform domain objects into PromptResult.
- PromptBuilders must not depend on RequestContext.
- PromptBuilders must never instantiate providers or access runtime state.

## Observability

- Observability is runtime-managed.
- Agents, Tools and Providers must not contain telemetry logic.
- TelemetryService is injected through RuntimeBootstrap.
- RuntimeOrchestrator owns span lifecycle.

## Timing

- Use time.perf_counter() for latency measurements.
- Do not use time.time() for execution duration.

## Dependency Injection

- All providers, builders and services are constructor injected.
- Avoid singleton services.

## Prompt Construction

- Prompt construction belongs in PromptBuilder implementations.
- Agents orchestrate; PromptBuilders format prompts.

##Validation Checklist

1. python -m compileall .
2. python scripts/test_runtime_workflow.py
3. Run any task-specific validation.
4. git status
5. git add .
6. git commit

## HTTP Infrastructure

All external HTTP communication must occur through HttpClient.

Design principles:

- Providers never call httpx directly.
- Providers translate generic HTTP exceptions into domain-specific exceptions.
- Runtime configuration flows:

Settings
→ ProviderConfig
→ HttpClient
→ Provider

This allows the same HTTP infrastructure to be reused by Search Providers and LLM Providers.