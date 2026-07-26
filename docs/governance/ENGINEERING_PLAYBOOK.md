# AI-Lab Engineering Playbook

**Version:** 2.0  
**Status:** Active  
**Owner:** AI-Lab Governance  
**Last Updated:** July 2026

---

# 1. Purpose

This document defines the standard sprint execution methodology for all projects within the AI-Lab workspace.

The objectives of this playbook are to:

- Standardize AI-assisted software development
- Maintain architectural integrity
- Prevent documentation drift
- Deliver production-ready software through small, iterative sprints
- Ensure every implementation is reviewed before being accepted

This document applies to every project in the AI-Lab workspace unless explicitly exempted.

---

# 2. Core Principles

## Documentation First

Implementation begins only after the required documentation has been reviewed.

---

## Architecture Before Code

Architecture drives implementation.

Implementation must never redefine architecture without approval.

---

## Small Iterative Sprints

Large initiatives are divided into manageable, reviewable sprints.

---

## Quality Over Velocity

Reliable software is preferred over rapid software.

---

## AI-Assisted Engineering

AI is treated as an engineering team with clearly defined responsibilities.

---

# 3. Roles & Responsibilities

## Product Owner

**Role:** Human

Responsibilities:

- Product vision
- Business priorities
- Sprint approval
- Final acceptance

---

## Principal Architect

**Primary AI:** ChatGPT

Responsibilities:

- Sprint planning
- Architecture review
- Documentation review
- Repository governance
- Technical debt assessment
- Sprint approval
- Long-term technical direction

---

## Software Engineer

**Primary AI:** Gemini CLI

Responsibilities:

- Feature implementation
- Refactoring
- Bug fixes
- Unit testing
- Build fixes
- Documentation updates

---

## Source of Truth

**Platform:** GitHub

Responsibilities:

- Version control
- Sprint history
- Documentation history
- Release history

---

## Local Development Environment

**Platform:** VS Code + Terminal + Git

Responsibilities:

- Build
- Test
- Local validation
- Commit
- Push

---

# 4. Sprint Lifecycle

```text
Sprint Planning
        │
        ▼
Documentation Review
        │
        ▼
Sprint Prompt Creation
        │
        ▼
Gemini Implementation
        │
        ▼
Quality Gate 1
(Local Validation)
        │
        ▼
Architecture Review
(ChatGPT)
        │
        ▼
Gemini Corrections
        │
        ▼
Quality Gate 2
(Build & Tests)
        │
        ▼
Git Commit
        │
        ▼
Push to GitHub
        │
        ▼
Quality Gate 3
(Repository Review)
        │
        ▼
Sprint Closed
```

No sprint skips a quality gate.

---

# 5. Sprint Planning

Every sprint must define:

- Sprint Goal
- Scope
- Out of Scope
- Deliverables
- Risks
- Dependencies
- Acceptance Criteria

---

# 6. Mandatory Reading Order

Before implementation begins, the Software Engineer must review the latest versions of:

## Workspace Governance

1. AI_LAB_PLAYBOOK.md
2. SPRINT_PLAYBOOK.md

## Project Governance

3. PROJECT.md
4. ENGINEERING.md
5. GEMINI.md
6. DECISIONS.md
7. PROJECT_STATUS.md

## Product Documentation

8. PRD.md
9. USER_STORIES.md
10. SOLUTION_ARCHITECTURE.md
11. DESIGN_SYSTEM.md

## Engineering Documentation

12. TECHNICAL_FOUNDATION.md
13. TOOLING_GUIDE.md

## Architecture Decisions

14. Relevant ADRs

---

# 7. Standard Sprint Prompt

Every sprint prompt must include:

- Role
- Sprint Objective
- Mandatory Reading
- Scope
- Constraints
- Files Allowed to Modify
- Files Not Allowed to Modify
- Validation Steps
- Documentation Updates
- Output Format
- Definition of Done
- Stop Conditions

---

# 8. Three Quality Gates

## Quality Gate 1 — Local Validation

Performed immediately after implementation.

Required checks:

- Build succeeds
- Linter passes
- No compilation errors
- No runtime errors
- Imports resolved
- Basic functionality verified

---

## Quality Gate 2 — Architecture Review

Performed by ChatGPT.

Review areas include:

- Architecture
- Code organization
- Maintainability
- Reusability
- Documentation consistency
- Technical debt
- Performance
- Security

Findings are categorized as:

- Critical
- Major
- Minor
- Suggestions

The Software Engineer addresses all required findings before code is committed.

---

## Quality Gate 3 — Repository Review

Performed after commit and push.

Review includes:

- Repository structure
- Documentation consistency
- Commit quality
- CHANGELOG
- PROJECT_STATUS
- Repository health
- Sprint completeness

Only after this review is the sprint officially closed.

---

# 9. Documentation Requirements

Documentation is part of implementation.

Mandatory updates:

- PROJECT_STATUS.md
- CHANGELOG.md

Update when affected:

- DECISIONS.md
- ADRs
- Architecture documentation
- Technical documentation
- User documentation

---

# 10. Definition of Done

A sprint is complete only when:

- Feature implemented
- Build passes
- Tests pass
- Documentation updated
- CHANGELOG updated
- PROJECT_STATUS updated
- Architecture review completed
- Repository review completed

---

# 11. Sprint Completion Report

The Software Engineer must provide:

- Summary
- Files Modified
- Validation Results
- Documentation Updated
- Known Limitations
- Recommendations for Next Sprint

---

# 12. Architecture Review Report

The Principal Architect provides:

- Architecture Assessment
- Repository Health
- Documentation Consistency
- Technical Debt
- Risks
- Improvement Opportunities
- Overall Score
- Approval Status

---

# 13. Sprint Scorecard

| Category | Max Score |
|----------|----------:|
| Functional Completion | 10 |
| Architecture Compliance | 10 |
| Code Quality | 10 |
| Documentation | 10 |
| Repository Health | 10 |
| Testing | 10 |
| Maintainability | 10 |

**Maximum Score:** 70

### Rating

- **65–70** — Excellent
- **55–64** — Good
- **45–54** — Acceptable
- **Below 45** — Rework Required

---

# 14. Git Workflow

```text
Software Engineer (Gemini)

        │
        ▼
Quality Gate 1
(Local Validation)

        │
        ▼
Architecture Review
(ChatGPT)

        │
        ▼
Gemini Corrections

        │
        ▼
Quality Gate 2
(Build & Tests)

        │
        ▼
Commit

        │
        ▼
Push

        │
        ▼
Quality Gate 3
(Repository Review)

        │
        ▼
Sprint Closed
```

---

# 15. Stop Conditions

A sprint must stop if:

- Architecture changes exceed approved scope.
- New ADRs are required.
- Critical build failures remain unresolved.
- Dependencies invalidate the sprint.
- Documentation becomes inconsistent.
- Major technical risks are identified.

Implementation resumes only after review and approval.

---

# 16. Continuous Improvement

This playbook is a living governance document.

It evolves alongside AI-Lab as new tools, engineering practices, and AI capabilities are adopted.

Changes to this playbook should be reviewed alongside **AI_LAB_PLAYBOOK.md** to ensure governance remains consistent across the entire workspace.