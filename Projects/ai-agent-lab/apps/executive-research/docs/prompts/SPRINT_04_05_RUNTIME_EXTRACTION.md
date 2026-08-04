# Sprint 4.5 – AI Agent Lab Runtime Extraction

## Role

You are a Principal Software Architect.

Your objective is to transform the current Executive Research architecture into a reusable AI Agent Lab platform.

This sprint is an architectural refactoring only.

Do NOT add new user-facing functionality.

---

# Background

Executive Research is the first showcase application.

AI Agent Lab is the platform.

The runtime must become completely independent from Executive Research.

---

# Mandatory Preparation

Read:

- docs/architecture/01-system-overview.md
- docs/architecture/02-repository-structure.md
- docs/architecture/03-request-lifecycle.md
- docs/architecture/04-agent-runtime.md

Review:

- apps/executive-research/backend
- current engine implementation

Understand the separation between:

- Product
- Workflow
- Runtime
- Provider

---

# Objectives

Extract all reusable orchestration components into a top-level `runtime` package.

Executive Research should only define:

- product APIs
- business validation
- workflow definition

Everything else belongs to the runtime.

---

# Target Repository Structure

Create:

runtime/

    engine/
        workflow_engine.py
        execution_context.py
        workflow.py

    interfaces/
        agent_runtime.py
        workflow.py

    agents/
        README.md

    providers/
        README.md

    telemetry/
        logger.py

shared/

    exceptions.py
    request_context.py

---

# Refactoring

Rename:

ResearchEngine

↓

WorkflowEngine

Rename:

RuntimeInterface

↓

AgentRuntime

Move reusable code into the runtime package.

The runtime must not import anything from:

apps/

No circular dependencies.

---

# Executive Research Workflow

Create:

apps/executive-research/backend/workflow/executive_research_workflow.py

Responsibilities:

- define workflow steps
- configure runtime
- map runtime output into product response

No provider logic.

---

# Service Responsibilities

ResearchService should only:

- validate business rules
- invoke ExecutiveResearchWorkflow
- return domain response

No orchestration logic.

---

# Runtime Responsibilities

WorkflowEngine:

- execute workflows
- coordinate agents
- manage execution context

AgentRuntime:

- abstract provider execution

Do NOT implement Gemini.

Provide a placeholder implementation only.

---

# Shared Layer

Move generic components into:

shared/

- exceptions
- request context
- common schemas

No application-specific code.

---

# Documentation

Update:

docs/architecture/

Reflect the new runtime structure.

Document:

- workflow lifecycle
- runtime responsibilities
- separation of concerns

---

# Validation

Run:

python -m compileall .

Verify:

- Backend compiles successfully
- POST /api/v1/research still works
- Frontend requires no changes
- Mock runtime still returns valid responses

---

# Constraints

Do NOT:

- integrate Gemini
- integrate OpenRouter
- add agents
- redesign APIs
- modify frontend

This sprint is architecture only.

---

# Implementation Report

Provide:

1. Files Created

2. Files Moved

3. Files Modified

4. Validation

5. Architectural Decisions

6. Remaining Work