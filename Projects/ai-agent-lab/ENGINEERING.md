# Engineering Practices

This document defines the engineering practices for the AI Agent Lab project.

## 1. Architecture First Principle
- Design before implementation.
- Major components must be reviewed (via ADRs) before significant code changes.

## 2. Engineering Principles
- **Modular Design:** Keep components small, decoupled, and single-responsibility.
- **Incrementalism:** Build one task at a time. Keep commits small.
- **Production-Ready:** Prioritize maintainability, testability, and explicit error handling.
- **Observability:** All LLM interactions and agent execution must be traceable.

## 3. Current Architecture
The AI Agent Lab uses a provider-based, DI-heavy architecture:
- **Composition Root**: `RuntimeBootstrap` is the sole entry point for assembling dependencies.
- **Runtime**: `RuntimeOrchestrator` manages execution flow; `Planner` generates `TaskGraph`s.
- **Agents**: Standardized via `BaseAgent` lifecycle.
- **Providers**: LLM and Search providers are abstracted via interfaces (`LLMProvider`, `SearchProvider`) for easy swapping.
- **Prompt Framework**: Separates `system_prompt` and `prompt`, enforces JSON schema contracts, and uses aggressive parsing for resilience.

## 4. Dependency Injection
- Components receive dependencies strictly via constructor injection.
- Components must NEVER construct their own dependencies.

## 5. Agent Responsibilities
- Agents execute business logic within `_execute()`.
- Agents must NOT select subsequent agents (orchestration belongs to `Runtime`).

## 6. Prompt & Response Contract
- Prompt construction is isolated in `PromptBuilder`.
- System/User prompt separation is strictly enforced to improve LLM compliance.
- LLM response contract is validated against JSON schemas at the `SummaryAgent` boundary.

## 7. Development Workflow
1. Read `docs/IMPLEMENTATION_TEMPLATE.md`.
2. Review architecture (ADRs).
3. Implement (small, localized).
4. Self-review.
5. Validate (Compile, Runtime, Smoke, E2E).
6. Commit.

## 8. Coding Standards
- Python 3.13+
- Strict type hinting.
- Docstrings for public components.
- Structured logging instead of `print()`.
- Fail-fast error propagation.

## 9. Repository Governance
- Repository Health Audit at sprint conclusion.
- Technical Debt and Recommendations are tracked.
