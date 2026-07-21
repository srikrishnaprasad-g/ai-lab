# Technical Debt Register

This register maintains a living record of known technical debt, improvements, and future architectural enhancements for the AI Agent Lab project.

| ID | Title | Area | Priority | Identified | Status | Reason |
|----|-------|------|----------|------------|--------|--------|
| TD-001 | Migrate test suite to pytest | Testing | Future | Sprint 5 | Open | Improve test discovery, reporting, fixtures and maintainability. |
| TD-002 | Consolidate smoke tests | Testing | Minor | Sprint 5 | Open | Reduce duplicated diagnostic execution and simplify maintenance. |
| TD-003 | System prompt integration in Mock Summary Agent | Agents | Minor | Sprint 5 | Open | Prepare the mock implementation for future LLM-backed execution. |
| TD-004 | RuntimeOrchestrator API evolution | Runtime | Future | Sprint 5 | Open | Introduce a single RuntimeOrchestrator.handle_request() entry point so callers remain unaware of agent selection and execution details. |
