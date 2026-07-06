This document will define the engineering practices for the AI Agent Lab project.

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
6. Run tests (when available).
7. Prepare for commit.

# AI-Assisted Development Workflow

Roles:

- ChatGPT: Staff Engineer / Architect
- Claude Code: Software Engineer
- User: Product Owner / Engineering Manager

Claude Code should:
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

A task is complete only if:

- Requirements are satisfied.
- Code is readable.
- No unnecessary complexity.
- Self-review completed.
- Ready to commit.

# Prompting Guidelines

Every implementation prompt should begin with:

"Read PROJECT.md and ENGINEERING.md before making changes."

Prompts should request only one logical task.

# Documentation Rules

Whenever architecture changes:

- Update PROJECT.md.
- Update ENGINEERING.md if engineering practices change.
- Update README.md if setup changes.

Write the document in professional Markdown suitable for an open-source project.

Do not modify any other files.