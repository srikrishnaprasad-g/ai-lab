# Technical Debt Register

This register maintains a living record of known technical debt, improvements, and future architectural enhancements for the AI Agent Lab project.

| ID | Title | Area | Priority | Identified | Status | Reason |
|----|-------|------|----------|------------|--------|--------|
| TD-001 | Migrate test suite to pytest | Testing | Future | Sprint 5 | Open | Improve test discovery, reporting, fixtures and maintainability. |
| TD-002 | Consolidate smoke tests | Testing | Minor | Sprint 5 | Open | Reduce duplicated diagnostic execution and simplify maintenance. |
| TD-003 | System prompt integration in Mock Summary Agent | Agents | Minor | Sprint 5 | Open | Prepare the mock implementation for future LLM-backed execution. |
| TD-004 | RuntimeOrchestrator API evolution | Runtime | Future | Sprint 5 | Open | Introduce a single RuntimeOrchestrator.handle_request() entry point so callers remain unaware of agent selection and execution details. |
| TD-005 | Observation ID references | Observability | Medium | Sprint 6 | Open | Ensure unique identification for spans and traces. |
| TD-006 | UTC timestamps | Observability | Medium | Sprint 6 | Open | Standardize all timing events to UTC. |
| TD-007 | Serialization tests | Testing | Medium | Sprint 6 | Open | Verify domain object serialization for context persistence. |
| TD-008 | Knowledge-gap heuristics | Planner | Medium | Sprint 6 | Open | Improve planning efficiency based on identified information gaps. |
| TD-009 | Summary synthesis improvements | Agents | Medium | Sprint 6 | Open | Refine summary quality and structure. |
| TD-010 | Finding title generation | Agents | Low | Sprint 6 | Open | Automate generation of descriptive titles for findings. |
| TD-011 | Implement external template loader for PromptRegistry | Prompts | Medium | Sprint 6 | Open | Support loading prompt templates from external files. |
| TD-012 | Evolve PromptResult to support structured fields | Prompts | Low | Sprint 6 | Open | Support separate system/user/metadata fields. |
| TD-013 | Implement CSS-like styling for PDFDocument | PDF | Low | Sprint 6 | Open | Move styling configuration out of code into templates. |
| TD-014 | Support DOCX/HTML via new PDFGenerator | PDF | Medium | Sprint 6 | Open | Implement alternative format renderers. |
| TD-015 | Remove obsolete mock_pdf_tool | Tools | Low | Sprint 6 | Open | Remove redundant mock PDF tool now replaced by ReportLabGenerator. |
