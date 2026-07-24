# Gemini CLI - Engineering Guide

This guide defines the development standards and workflow for the AI Agent Lab project.

## 1. Implementation Workflow
1. **Mandatory Preparation**: Review `PROJECT.md`, `ENGINEERING.md`, `DECISIONS.md`, and relevant `docs/` design docs.
2. **Design Review**: If the task changes architecture, draft an ADR.
3. **Implementation**: Follow `BaseAgent` and `RuntimeOrchestrator` contracts.
4. **Validation**: Execute compile, unit, integration, and end-to-end tests.
5. **Self-Review**: Verify against Engineering Principles.
6. **Delivery**: Commit (logical grouping) and Tag.

## 2. Architectural Guard Rails
- **Architecture Freeze**: Do not redesign the runtime during implementation sprints.
- **Dependency Injection**: Use constructor injection exclusively.
- **Provider Abstraction**: Access external services (LLM, Search) only through defined Provider interfaces.
- **Prompt Separation**: Always use `SummaryPromptBuilder` to separate system/user instructions.
- **JSON Contract**: Enforce structured JSON schema validation at the parsing boundary.

## 3. Coding Standards
- Python 3.13+
- Type hints: Mandatory for all public methods and data structures.
- Logging: Use structured logging (`logging` module). Avoid `print()`.
- Error Handling: Fail fast, propagate explicit errors, validate contracts, and log diagnostic details.

## 4. Validation Policy
A task is complete only when:
- `py_compile` succeeds.
- All relevant integration/E2E tests pass.
- Repository health check passes.
- Documentation (PROJECT.md, DECISIONS.md) updated.

## 5. Definition of Done
- All tests pass (Unit/Integration/E2E).
- Documentation updated and verified.
- Technical debt recorded (or resolved).
- Repository health audit clean.
- Git commit created.

## 6. Stop Conditions
- Undocumented architectural change.
- Conflicting implementation logic.
- Material difference between implementation and documentation.
- Validation failure.
*If any stop condition occurs, initiate an investigation report before proceeding.*

## 7. Lessons Learned (Sprint 7 & 8)
- **Prompt Engineering**: Separating system instructions (`systemInstruction`) significantly improves JSON compliance.
- **Robust Parsing**: Raw LLM output often requires regex-based JSON extraction to handle conversational verbosity.
- **Observability**: Stage-by-stage tracing in verbose mode is essential for debugging production workflows.
- **Credential Protection**: Always route API urls and headers through masking utilities (`mask_api_key`) before writing to any log stream.
- **Clean Output Philosophy**: Maintain strict separation between user-facing presentation and developer-oriented debugging. Never print raw dataclasses (e.g., `PDFResult(...)`) in default normal mode. Use clean, formatted markdown or block-based summaries instead.
