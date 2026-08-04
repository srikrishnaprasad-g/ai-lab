# Sprint 4.6 – Workflow Layer & Composition Root

## Role

You are a Principal Software Architect.

You are working on AI Agent Lab, a reusable multi-agent platform.

Executive Research is the first showcase application built on top of the platform.

This sprint establishes the final application boundary before AI integration.

No new user-facing functionality should be added.

---

# Architecture Goal

Current architecture:

API
↓

ResearchService
↓

WorkflowEngine
↓

AgentRuntime

Target architecture:

API
↓

ResearchService
↓

ExecutiveResearchWorkflow
↓

WorkflowEngine
↓

AgentRuntime

The Workflow belongs to the application.

The Engine belongs to the platform.

---

# Mandatory Preparation

Read:

docs/architecture/01-system-overview.md

docs/architecture/02-repository-structure.md

docs/architecture/03-request-lifecycle.md

docs/architecture/04-agent-runtime.md

docs/architecture/05-backend-architecture.md

Review:

runtime/

shared/

apps/executive-research/backend/

Understand the separation between:

Application

Workflow

Runtime

Provider

---

# Objectives

Introduce an explicit Workflow layer.

Introduce a Composition Root.

Move object construction out of API routes.

Do not integrate Gemini.

---

# Create

apps/executive-research/backend/workflow/

    executive_research_workflow.py

Responsibilities:

- define workflow execution

- invoke WorkflowEngine

- convert RuntimeResult into ResearchResponse

- contain no provider logic

---

# Composition Root

Create:

apps/executive-research/backend/dependencies.py

Responsibilities:

- instantiate MockAgentRuntime

- instantiate WorkflowEngine

- instantiate ExecutiveResearchWorkflow

- instantiate ResearchService

Provide reusable dependency functions.

Routes should never construct objects directly.

---

# Research Service

Responsibilities:

- business validation

- invoke ExecutiveResearchWorkflow

- return domain objects

Nothing else.

---

# Workflow Layer

Responsibilities:

- prepare execution context

- invoke WorkflowEngine

- transform runtime output

- remain independent of providers

---

# WorkflowEngine

Do not modify its responsibilities.

It remains platform infrastructure.

---

# AgentRuntime

No changes.

Still use MockAgentRuntime.

---

# API Layer

Refactor routes to use dependency injection from dependencies.py.

No manual object construction.

---

# Documentation

Update:

docs/architecture/

Document:

- Application Workflow

- Composition Root

- Dependency Flow

---

# Validation

Run:

python -m compileall .

Verify:

POST /api/v1/research

still returns mocked data.

Frontend requires no changes.

---

# Constraints

Do NOT

- integrate Gemini

- create agents

- introduce LangGraph

- redesign API contracts

- modify frontend

---

# Implementation Report

Provide

1. Files Created

2. Files Modified

3. Dependency Graph

4. Validation

5. Architectural Decisions

6. Remaining Work