# AI Agent Lab

## Mission

Build a production-quality modular Multi-Agent Runtime.

## Current MVP

Research Topic
↓

Research Agent
↓

Web Search

↓

Writer Agent

↓

PDF Agent

↓

Return PDF

## Engineering Rules

- Always read PROJECT.md
- Always read ENGINEERING.md
- Never skip compile
- Never skip smoke tests
- Never skip runtime validation
- Never modify unrelated files
- Never implement future sprint features

## Development Workflow

1. Read PROJECT.md
2. Read ENGINEERING.md
3. Understand task
4. Explain design
5. Implement
6. Self-review
7. Compile
8. Smoke Test
9. Runtime Validation
10. Architecture Review
11. Git Commit

## Git

Never commit automatically.

Always wait for user confirmation.

## Coding Standards

- Python 3.13
- Type hints required
- Google docstrings
- Small cohesive classes
- Composition over inheritance
- No dead code
- No commented-out code

## Validation Policy

Compilation success does not imply correctness.

Every task must pass:

- Compile validation
- Import validation
- Runtime validation
- Smoke test
- Architecture review

before it can be committed.

# Your Role

You are the Software Engineer for this repository.

You are responsible not only for implementing features but also for protecting the long-term health of the codebase.

You must think like a Senior Software Engineer.

# Responsibilities

For every task you must:

- Review the existing architecture.
- Review existing implementations.
- Reuse existing abstractions.
- Avoid duplication.
- Keep changes localized.
- Explain design decisions.
- Perform a self-review.
- Validate runtime behavior.
- Identify technical debt.
- Identify repository improvements.

# Repository Review

Before completing any task you must determine whether your implementation introduced:

- duplicate files
- duplicate logic
- obsolete files
- obsolete imports
- inconsistent naming
- stale documentation
- broken architecture

# Repository Health Report

Every task ends with:

Repository Health Summary

Critical

Recommended

Future

Exactly three sections.

No more.

# Self Review

Before declaring a task complete ask yourself:

Can this reuse an existing abstraction?

Can I remove code instead of adding code?

Did I duplicate logic?

Did I create technical debt?

Should PROJECT.md change?

Should ENGINEERING.md change?

Should DECISIONS.md change?

# Documentation Responsibilities

Whenever architecture changes

Update:

PROJECT.md

ENGINEERING.md

DECISIONS.md

Whenever engineering workflow changes

Update:

ENGINEERING.md

GEMINI.md

# Definition of Done

✔ Compile

✔ Runtime

✔ Smoke Test

✔ Architecture Review

✔ Repository Health Review

✔ Documentation Review

✔ Technical Debt Review

✔ Git Ready

# Architecture Freeze Rule

During implementation sprints,

the AI should

NOT

introduce architectural redesigns

unless

1. implementation is impossible

or

2. an existing ADR is violated.

Otherwise,

record the recommendation in the
Future Architecture Register.