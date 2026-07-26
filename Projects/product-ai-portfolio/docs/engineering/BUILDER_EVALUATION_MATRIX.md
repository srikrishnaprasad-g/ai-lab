---
title: Builder Evaluation Matrix
status: Accepted
version: 1.0
date: 2026-07
owner: AI-Lab
review: 2027-07
---

# Builder Evaluation Matrix

## Purpose

The Builder Evaluation Matrix provides a standardized framework for evaluating technologies, AI platforms, frameworks, development tools, libraries, and services before they are adopted into AI-Lab.

Rather than selecting tools based solely on popularity or personal preference, AI-Lab evaluates candidates against consistent engineering principles.

---

# Guiding Principles

Technology adoption should be:

- Objective
- Repeatable
- Transparent
- Vendor-independent
- Aligned with AI-Lab architecture

The goal is long-term engineering sustainability rather than short-term convenience.

---

# Evaluation Process

Every candidate should be evaluated using the following stages.

1. Identify the engineering need.
2. Shortlist candidate solutions.
3. Evaluate each candidate using the Builder Evaluation Matrix.
4. Document the decision.
5. Create or update an ADR if the architecture changes.
6. Update the Tooling Guide if adoption is approved.

---

# Evaluation Dimensions

| Dimension | Description | Weight |
|------------|-------------|---------|
| Strategic Alignment | Supports AI-Lab engineering principles | High |
| Technical Fit | Integrates well with the existing architecture | High |
| Developer Experience | Improves productivity and usability | High |
| Maintainability | Sustainable over the long term | High |
| Vendor Independence | Minimizes lock-in risk | Medium |
| Community & Ecosystem | Mature ecosystem and active community | Medium |
| Documentation Quality | Availability of reliable documentation | Medium |
| Security & Privacy | Meets engineering security expectations | High |
| Cost Efficiency | Value relative to cost | Medium |
| Learning Curve | Ease of adoption for contributors | Low |

---

# Recommended Scoring Scale

| Score | Interpretation |
|---------|----------------|
| 5 | Excellent |
| 4 | Good |
| 3 | Acceptable |
| 2 | Weak |
| 1 | Poor |

---

# Example Evaluation Template

| Dimension | Weight | Score | Notes |
|------------|---------|------|------|
| Strategic Alignment | High | | |
| Technical Fit | High | | |
| Developer Experience | High | | |
| Maintainability | High | | |
| Vendor Independence | Medium | | |
| Community | Medium | | |
| Documentation | Medium | | |
| Security | High | | |
| Cost | Medium | | |
| Learning Curve | Low | | |

---

# Adoption Criteria

A technology should normally be adopted when it:

- Solves a clearly defined engineering problem.
- Aligns with AI-Lab principles.
- Demonstrates long-term sustainability.
- Improves developer productivity.
- Does not introduce unnecessary architectural complexity.

---

# Review Frequency

Technology decisions should be re-evaluated:

- During annual architecture reviews.
- Before major platform migrations.
- When significant ecosystem changes occur.

---

# Related Documents

- ADR-002
- ADR-008
- TOOLING_GUIDE.md