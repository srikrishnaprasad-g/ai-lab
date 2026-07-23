# Git Recovery Plan

This plan outlines the logical commit sequence to finalize Sprint 7 and synchronize the repository.

## Commit Sequence

### Commit 1: Refactor Prompt Framework
- **Title**: `refactor(prompts): update to production system/user prompts`
- **Purpose**: Refactor prompt templates for strict JSON adherence and proper system/user separation.
- **Files**: `prompts/templates.py`, `prompts/summary_prompt_builder.py`
- **Reasoning**: Foundation for LLM compliance.

### Commit 2: Implement Production LLM Integration
- **Title**: `feat(llm): implement production LLM integration`
- **Purpose**: Replace simulated `SummaryAgent` logic with production Gemini provider calls via DI.
- **Files**: `agents/summary/summary_agent.py`, `agents/agent_factory.py`, `runtime/runtime_bootstrap.py`, `llm/providers/gemini_provider.py`, `cli.py`
- **Reasoning**: Core feature implementation for production summary generation.

### Commit 3: Fix Prompt Test Suite
- **Title**: `fix(test): resolve QE-001 prompt testing failure`
- **Purpose**: Update tests to reflect prompt template API changes.
- **Files**: `tests/test_prompt_framework.py`
- **Reasoning**: Resolve blocking test failure identified during hardening.

### Commit 4: Document Architectural Decisions
- **Title**: `chore(docs): document Sprint 7 architectural decisions`
- **Purpose**: Record new ADRs and architecture delta.
- **Files**: `docs/adr-017.md`, `DECISIONS.md`, `docs/ARCHITECTURE_DELTA_SPRINT7.md`, `docs/LLM_RESPONSE_CONTRACT.md`
- **Reasoning**: Maintain architectural history.

### Commit 5: Finalize Documentation and Governance
- **Title**: `chore(status): finalize Sprint 7 documentation and health reports`
- **Purpose**: Synchronize project status, history, and health reports.
- **Files**: `PROJECT_STATUS.md`, `docs/TECHNICAL_DEBT.md`, `CHANGELOG.md`, `RELEASE_NOTES.md`, `docs/SPRINT_HISTORY.md`, `docs/REPOSITORY_HEALTH_REPORT.md`, `docs/GIT_RECOVERY_PLAN.md`, `ENGINEERING.md`, `GEMINI.md`
- **Reasoning**: Ensure project governance completeness.

## Final Action
After commits 1-5, tag the repository: `git tag v0.6.0-rc1`
