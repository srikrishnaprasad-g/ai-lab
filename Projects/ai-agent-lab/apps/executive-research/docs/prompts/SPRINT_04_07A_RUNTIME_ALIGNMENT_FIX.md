Important: If, during implementation, you discover that the existing AI Agent Lab runtime does not expose a public entry point capable of executing the complete Planner → Research → Summary → PDF pipeline, do not invent one. Instead, stop and produce a gap analysis listing:

The missing runtime capability.
The existing runtime components reviewed.
The minimal change required inside AI Agent Lab to expose the capability.
Why that change is preferable to duplicating logic in the web application.

# Sprint 4.7A — Runtime Alignment Fix

## Sprint Type

**Architecture Correction Sprint**

This is a small corrective sprint.

Its only objective is to align the Executive Research web backend with the existing AI Agent Lab runtime.

No new features should be added.

No runtime redesign should occur.

---

# Background

The previous sprint introduced `AIAgentLabFacade`, which is the correct architectural direction.

However, the facade currently recreates parts of the AI Agent Lab runtime by constructing:

- TaskGraph
- WorkflowDefinition
- ExecutionPlan
- Request IDs
- Runtime Context

These responsibilities already belong to the AI Agent Lab runtime.

The goal of this sprint is to remove those duplications.

---

# Mandatory Preparation

Before making any code changes, read:

- PROJECT.md
- ENGINEERING.md
- DECISIONS.md
- PROJECT_STATUS.md
- CHANGELOG.md

Review:

- runtime/
- RuntimeBootstrap
- RuntimeOrchestrator
- Planner
- Existing Runtime models
- Existing Runtime execution flow

Do not assume anything.

Reuse existing runtime behaviour.

---

# Guiding Principle

The web application must never reconstruct or duplicate runtime behaviour.

If AI Agent Lab already provides the functionality, reuse it.

The runtime owns execution.

The web application owns HTTP.

---

# Objective

Transform `AIAgentLabFacade` into a thin adapter.

The facade should simply invoke the existing AI Agent Lab runtime.

It should not recreate runtime objects.

---

# Responsibilities

## FastAPI

Responsible for:

- HTTP
- Validation
- Response serialization

Nothing else.

---

## ResearchService

Responsible for:

- Business validation
- Calling AIAgentLabFacade

Nothing else.

---

## AIAgentLabFacade

Responsible for:

- Invoking RuntimeBootstrap
- Waiting for completion
- Mapping RuntimeResult to ResearchResponse

Nothing else.

---

## AI Agent Lab Runtime

Responsible for:

- Workflow creation
- Planner
- Task graph
- Execution plan
- Context
- Runtime orchestration
- Agent execution
- Provider execution
- Artifact generation

Do not duplicate any of these responsibilities.

---

# Required Corrections

## 1. Remove Manual Workflow Construction

Remove any code that manually creates:

- TaskGraph
- WorkflowDefinition
- ExecutionPlan

These must come from AI Agent Lab runtime.

---

## 2. Remove Manual Context Creation

Remove any code that creates:

- request_id
- correlation_id
- TypedWorkflowContext

These already belong to the runtime.

---

## 3. Remove Runtime Knowledge

The facade must not access:

```python
context.get(...)
```

or inspect runtime internals.

Instead, consume the existing RuntimeResult returned by the runtime.

---

## 4. RuntimeBootstrap

The facade should invoke RuntimeBootstrap using the existing public runtime entry point.

Do not bypass RuntimeBootstrap.

Do not instantiate RuntimeOrchestrator directly unless RuntimeBootstrap already does so.

---

## 5. RuntimeResult

If RuntimeBootstrap already returns RuntimeResult, use it directly.

Do not reconstruct response objects from runtime context.

---

## 6. PDF Download

Do not hardcode:

```text
reports/{filename}
```

Instead:

Use the PDF artifact/path already produced by the runtime.

Return a download URL that references the generated artifact.

---

## 7. Repository Cleanup

Remove any duplicate runtime code introduced during Sprint 4.7.

Remove:

- unused imports
- duplicate models
- obsolete helper methods
- dead code

Do not remove reusable runtime components.

---

# Validation

Verify that the complete execution path becomes:

```text
User

↓

React

↓

FastAPI

↓

ResearchService

↓

AIAgentLabFacade

↓

RuntimeBootstrap

↓

RuntimeOrchestrator

↓

Planner

↓

ResearchAgent

↓

Search Provider (Tavily)

↓

SummaryAgent

↓

Gemini

↓

PDFAgent

↓

RuntimeResult

↓

ResearchResponse

↓

React
```

There should be no duplicate orchestration anywhere inside the web application.

---

# Documentation

Update:

- PROJECT_STATUS.md
- CHANGELOG.md

Do NOT mark the project as complete.

Instead update:

Sprint 4.7A completed.

Architecture fully aligned with AI Agent Lab runtime.

---

# Repository Health Review

Before completing the sprint, verify:

- No duplicate orchestration
- No duplicate runtime models
- No duplicate execution context
- No duplicate workflow creation
- No dead code
- No unused imports

---

# Definition of Done

This sprint is complete only when:

- The web application no longer recreates runtime behaviour.
- RuntimeBootstrap is the single runtime entry point.
- RuntimeOrchestrator remains the only orchestrator.
- Planner remains inside AI Agent Lab.
- TaskGraph is owned by AI Agent Lab.
- WorkflowDefinition is owned by AI Agent Lab.
- ExecutionPlan is owned by AI Agent Lab.
- RuntimeResult is returned by the runtime.
- FastAPI acts only as an HTTP adapter.
- React UI requires no changes.
- API contract remains unchanged.
- Repository health passes.

---

# Stop Conditions

Stop immediately if any of the following occur:

- Runtime redesign becomes necessary.
- RuntimeBootstrap requires breaking changes.
- RuntimeOrchestrator must be modified.
- Existing runtime contracts need changing.
- New orchestration layers are introduced.
- Existing AI Agent Lab functionality is duplicated.

Produce an investigation report instead of continuing implementation.

---

# Implementation Report

Provide:

1. Executive Summary
2. Files Created
3. Files Modified
4. Files Removed
5. Runtime Components Reused
6. Duplicate Components Removed
7. Integration Flow
8. Validation Results
9. Repository Health Findings
10. Remaining Work

---

# Success Criteria

At the end of this sprint, the Executive Research web application should behave as a thin HTTP adapter over the existing AI Agent Lab runtime.

No orchestration logic should exist outside the runtime.

No runtime behaviour should be duplicated.

The architecture should now faithfully represent the original AI Agent Lab design.