---
title: Tooling Guide
status: Accepted
version: 1.0
date: 2026-07
owner: AI-Lab
review: 2027-07
---

# Tooling Guide

## Purpose

This guide defines the standard tools used throughout AI-Lab and the responsibilities assigned to each.

The objective is to ensure contributors consistently use the most appropriate tool for each stage of the development lifecycle.

---

# Engineering Philosophy

No single platform is considered the best at every task.

AI-Lab adopts a role-based tooling strategy where each platform is selected according to its strengths.

---

# Standard Toolchain

| Activity | Primary Tool |
|-----------|--------------|
| Product Strategy | ChatGPT |
| Product Discovery | ChatGPT |
| PRD Creation | ChatGPT |
| Solution Architecture | ChatGPT |
| Engineering Reviews | ChatGPT |
| Architecture Reviews | ChatGPT |
| Documentation | ChatGPT |
| UX Exploration | Google AI Studio |
| Visual Brainstorming | Google AI Studio |
| Screenshot Reviews | Google AI Studio |
| Software Implementation | Gemini CLI |
| Repository-wide Refactoring | Gemini CLI |
| Multi-file Editing | Gemini CLI |
| UI Component Generation | v0 (Optional) |
| Rapid MVPs | Lovable (Optional) |
| Version Control | GitHub |
| Deployment | Vercel |

---

# Tool Responsibilities

## ChatGPT

Primary responsibilities:

- Product Management
- Product Strategy
- Architecture
- Documentation
- Engineering Reviews
- Design Reviews

---

## Google AI Studio

Primary responsibilities:

- UX ideation
- Layout exploration
- Visual experimentation
- Prompt testing

---

## Gemini CLI

Primary responsibilities:

- Feature implementation
- Bug fixes
- Refactoring
- Sprint execution

---

## GitHub

Primary responsibilities:

- Repository management
- Pull Requests
- Releases
- Collaboration

---

## Vercel

Primary responsibilities:

- Preview deployments
- Production deployments
- Rollbacks

---

# Tool Selection Principles

- Use the best tool for the task.
- Avoid overlapping responsibilities.
- Prefer replaceable solutions.
- Document major tooling changes through ADRs.

---

# Introducing New Tools

Before adopting a new platform:

1. Complete the Builder Evaluation Matrix.
2. Review architectural impact.
3. Update relevant ADRs if required.
4. Update this guide.

---

# Related Documents

- ADR-001
- ADR-002
- ADR-008
- BUILDER_EVALUATION_MATRIX.md