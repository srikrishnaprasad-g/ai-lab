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

A task is complete only when ALL of the following are satisfied.

## Design

- Requirement understood
- Architecture reviewed
- Existing implementation reviewed

## Implementation

- Code complete
- Type hints added
- Docstrings added
- Error handling implemented

## Validation

- Compile succeeds
- Imports validated
- Runtime validation passes
- Smoke test passes

## Repository

- Repository health reviewed
- No Critical issues introduced
- Git status clean

## Documentation

- PROJECT.md updated
- ENGINEERING.md updated
- DECISIONS.md updated (if architecture changed)
- GEMINI.md updated (if workflow changed)

## Technical Debt

- New debt recorded
- Recommendations recorded
- Future improvements recorded

## Delivery

- Git commit
- Git tag

Sprint 4+

Architecture compliance

Agent contract compliance

Execution pipeline validation

Planning validation

Integration validation
-----

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

## Documentation Rules

Whenever architecture changes:

- Update PROJECT.md.
- Update ENGINEERING.md if engineering practices change.
- Update README.md if setup changes.
- Update TECHNICAL_DEBT.md if new technical debt is introduced or resolved.


Write the document in professional Markdown suitable for an open-source project.

Do not modify any other files.

## Repository Hygiene

Before every commit:

- Review git status.
- Remove generated artifacts from version control.
- Never commit __pycache__, logs, temporary files, or IDE metadata.
- Prefer small, logically grouped commits over large mixed commits.

## Agent Design
For detailed agent implementation guidelines, reference `docs/AGENT_DESIGN.md`. All production agents must follow the standardized `BaseAgent` lifecycle and integration patterns defined therein.

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

## Engineering Notes – Sprint 3.8

### Configuration Refactor

The LLM configuration layer was simplified to eliminate duplicate configuration paths.

Changes:

- Introduced `DEFAULT_LLM_PROVIDER`
- Introduced `DEFAULT_LLM_MODEL`
- Introduced `DEFAULT_LLM_TIMEOUT`
- Removed legacy provider/model configuration
- Added explicit model support to `LLMProviderConfig`

### Provider Architecture

Current architecture:

Settings
↓
LLMProviderFactory
↓
LLMProviderConfig
↓
Provider
↓
HttpClient
↓
Provider API
↓
ResponseMapper
↓
LLMResponse

All providers should follow this architecture.

### Gemini Provider

Implemented production Gemini integration.

Features:

- configurable model
- configurable timeout
- configurable API version
- configurable base URL
- centralized authentication
- standardized response mapping
- provider-specific exception handling

### Lessons Learned

During implementation several architectural issues were discovered and resolved:

- Optional (`str | None`) environment variable parsing
- deterministic `.env` loading
- provider configuration duplication
- hardcoded provider model
- package import inconsistencies
- provider factory wiring

These improvements now make adding future providers (Groq, OpenAI, OpenRouter, Anthropic, Ollama) straightforward.

# Engineering Guard Rails

The following rules apply to every implementation.

## Configuration

- Configuration must have a single source of truth.
- Duplicate configuration paths are prohibited.
- Components must never read environment variables directly.

## Dependency Injection

- RuntimeBootstrap is the composition root.
- Factories are only used by RuntimeBootstrap.
- Business logic must never instantiate providers.

## Providers

- Providers own external communication.
- Business logic never calls HTTP clients directly.
- Provider-specific logic never leaks into Agents or Tools.

## Imports

- No broken imports.
- No circular imports.
- Package exports must remain consistent.

## Files

- No duplicate implementations.
- No obsolete files.
- No commented-out code.
- No dead code.

## Documentation

Architecture changes require updates to:

- PROJECT.md
- ENGINEERING.md
- DECISIONS.md

Implementation changes affecting AI workflows require GEMINI.md updates.

-----
# Technical Debt Register

| ID | Description | Priority | Status | Target Sprint |
|----|-------------|----------|--------|---------------|

Example

TD-001

Move HttpClient to infra package

Medium

Open

Sprint 6

-----

# Recommendations Register

| ID | Recommendation | Status | Sprint |
|----|---------------|--------|--------|

Status

Open
Accepted
Rejected
Completed

------

# Future Architecture Register

| ID | Improvement | Planned Sprint | Status |

-------

# Runtime Responsibilities

Runtime owns:

- orchestration
- planning
- lifecycle
- retries
- telemetry
- execution policies

Agents own:

- business logic
- tool usage
- context enrichment

Agents must never perform orchestration.

-------

# Execution Pipeline

All cross-cutting concerns execute through the pipeline.

Examples

Telemetry

Retry

Timeout

Future

Authorization

Caching

Rate Limiting

Auditing

------

# Planning

Planning determines

WHAT executes.

Execution determines

HOW it executes.

Agents perform

THE WORK.

These responsibilities must remain separate.

-----

# Agent Contract

Every Agent must

Validate Input

Execute

Return AgentResult

Never select another agent

Never terminate the workflow

Never own orchestration.

----- 

# Runtime Contracts

AgentId
ExecutionAction
ExecutionDecision
AgentResult
RuntimeResult

-----

# Runtime Layering

RuntimeBootstrap
    ↓
RuntimeOrchestrator
    ↓
Planner
    ↓
ExecutionPipeline
    ↓
PipelineStages
    ↓
Callback

-----

# Responsibilities Boundaries

| Component           | Responsibility           |
| ------------------- | ------------------------ |
| Planner             | Decide what happens next |
| RuntimeOrchestrator | Coordinate execution     |
| ExecutionPipeline   | Execute middleware chain |
| PipelineStage       | Cross-cutting concerns   |
| Callback            | Business logic           |

------

# Runtime Architecture

RuntimeBootstrap
        │
        ▼
RuntimeOrchestrator
        │
        ▼
Planner
        │
        ▼
ExecutionPipeline
        │
        ▼
TelemetryStage
        │
        ▼
RetryStage
        │
        ▼
Callback

----

# Composition Root

RuntimeBootstrap is the sole composition root.
All runtime dependencies are assembled there.
Other runtime components receive dependencies via constructor injection.
----

# Dependency Injection Convention

RuntimeOrchestrator never constructs dependencies.
Planner never constructs dependencies.
ExecutionPipeline never constructs dependencies.
----

# Pipeline Construction Order

ExecutionPipeline
    ↓
TelemetryStage
    ↓
RetryStage
    ↓
Callback
----