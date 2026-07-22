# IMPLEMENTATION_TEMPLATE.md

This document defines the mandatory protocol for all implementation tasks in the AI Agent Lab project. All engineers (human or AI) MUST follow this template.

## 1. Mandatory Preparation
Before making ANY changes, completely read:
- PROJECT.md
- PROJECT_STATUS.md
- ENGINEERING.md
- GEMINI.md
- DECISIONS.md
- docs/TECHNICAL_DEBT.md
- Relevant `docs/` design documents (e.g., AGENT_DESIGN.md, PROMPT_DESIGN.md).

Review the implementation of the most recent related sprints.

## 2. Architecture Review
Review the current implementation and verify:
- Compatibility with existing architectural principles.
- Responsibilities of the target component.
- Compliance with ADRs.

## 3. Architecture Validation
Answer the following questions BEFORE implementation begins:
1. **Prompt Ownership:** Where should new prompt templates reside and why?
2. **Execution Lifecycle:** Describe the request-to-result flow for this change.
3. **Responsibility Boundaries:** Define the clear boundaries between agents, prompt builders, and LLM providers for this task.
4. **Validation Strategy:** Describe the specific unit and behavioral tests required for this task.

## 4. Implementation Gate
- All architecture questions answered?
- Existing architecture compliant?
- Responsibilities clearly separated?
(Implementation MUST NOT begin until all conditions are satisfied).

## 5. Implementation Objectives
Define the primary goals of the task.

## 6. Constraints
List what MUST NOT be modified or redesigned, including architectural freezes.

## 7. Validation
Required validation steps:
- compile validation
- static validation
- unit tests
- integration tests (if applicable)

## 8. Documentation Review
List all documents that require updates (e.g., PROJECT.md, PROMPT_DESIGN.md, etc.).

## 9. Repository Health Review
Plan for reviewing/fixing:
- dead code
- duplicate logic
- architectural inconsistencies
- obsolete framework code

## 10. Technical Debt Review
- Review for new technical debt.
- Record in `docs/TECHNICAL_DEBT.md` using the standard format.

## 11. Completion Gates
- All architectural questions answered
- Implementation complete
- Tests passing
- Documentation synchronized
- Repository health maintained
- Definition of Done satisfied

## 12. Output Format
- Architecture Review
- Architecture Validation Answers
- Files Reviewed
- Files Modified
- Implementation Summary
- Validation Results
- Documentation Review
- Repository Verification
- Repository Health
- Technical Debt Updates
- Outstanding Issues
- Definition of Done

## 13. Stop Conditions
List conditions that require stopping implementation immediately.

## 14. Continuous Improvement
Record any insights to improve the engineering process.

## 15. Post-Implementation Reflection
- What architectural decisions were made?
- What trade-offs were accepted?
- What technical debt remains?
- What should the next sprint know?
