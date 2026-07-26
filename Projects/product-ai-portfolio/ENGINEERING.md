# Engineering Guide

## Purpose

This document defines the engineering standards specific to the Product AI Portfolio project.

Global engineering standards are defined in the AI-Lab workspace documentation.

This document captures only project-specific guidance.

---

# Required Reading Order

Before making implementation changes, review:

1. GEMINI.md
2. PROJECT.md
3. PRD
4. Solution Architecture
5. Design System
6. Relevant ADRs

---

# Engineering Principles

This project follows:

- Documentation First
- Architecture Before Code
- Component Reuse
- Simplicity
- Maintainability

---

# Development Workflow

Planning

↓

Architecture Review

↓

Implementation

↓

Validation

↓

Documentation Update

↓

Commit

---

# Coding Standards

- TypeScript Strict Mode
- Functional Components
- Server Components where appropriate
- Strong typing
- No duplicated logic
- Small reusable components

---

# Folder Organization

The source tree should follow the approved repository architecture.

Feature-based organization is preferred over file-type organization.

---

# Testing Expectations

Every completed feature should be:

- Buildable
- Type-safe
- Responsive
- Accessible

---

# Documentation Expectations

Every implementation sprint updates:

- PROJECT_STATUS.md
- CHANGELOG.md

When architecture changes:

- ADRs
- Technical documentation

must also be updated.

---

# Definition of Done

A sprint is complete when:

- Implementation is complete.
- Documentation updated.
- Quality gates passed.
- Ready for architecture review.

---

# References

Workspace Engineering

../../../ENGINEERING.md

Technical Foundation

docs/engineering/TECHNICAL_FOUNDATION.md