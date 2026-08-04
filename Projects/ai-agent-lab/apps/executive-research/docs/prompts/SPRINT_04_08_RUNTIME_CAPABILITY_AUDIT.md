# Sprint 4.8 — AI Agent Lab Runtime Capability Audit

## Sprint Type

Architecture Audit

This is NOT an implementation sprint.

This sprint exists to verify the existing AI Agent Lab runtime before any further web integration.

No architectural redesign should occur.

No new runtime behaviour should be introduced.

---

# Background

Executive Research is the first web application built on top of AI Agent Lab.

Recent implementation attempts introduced duplicate orchestration because assumptions were made about the runtime API.

This sprint exists to eliminate assumptions.

The runtime itself is the source of truth.

---

# Role

You are acting as a Principal Engineer performing an architectural audit.

Your objective is to determine whether the existing AI Agent Lab runtime already exposes the capabilities required by the Executive Research web application.

Do not modify behaviour until the investigation is complete.

---

# Mandatory Preparation

Read completely:

PROJECT.md

ENGINEERING.md

DECISIONS.md

README.md

PROJECT_STATUS.md

CHANGELOG.md

Review the entire runtime directory before making any modifications.

---

# Audit Objectives

Determine whether the runtime already owns:

- Workflow creation
- Execution context creation
- TaskGraph construction
- WorkflowDefinition creation
- ExecutionPlan creation
- Planner execution
- Runtime orchestration
- Provider invocation
- RuntimeResult creation

Do not assume ownership.

Verify ownership from the existing implementation.

---

# Required Investigation

Answer each question with evidence.

## 1.

Does RuntimeBootstrap expose a public execution API?

Examples:

execute()

run()

execute_workflow()

execute_research()

or similar.

If yes

Document:

- method
- signature
- caller

If no

Document that the capability is missing.

---

## 2.

Who currently creates WorkflowDefinition?

Possible answers:

Runtime

Planner

Application

Nobody

Provide file names.

---

## 3.

Who currently creates TaskGraph?

Provide file names.

---

## 4.

Who currently creates ExecutionPlan?

Provide file names.

---

## 5.

Who owns TypedWorkflowContext?

Determine whether:

- Runtime creates it

or

- Application creates it

or

- Nobody currently owns it

Provide evidence.

---

## 6.

Who owns RuntimeResult?

Determine:

- where it is created
- who consumes it
- whether the web application should receive it directly

---

## 7.

Who currently invokes:

Planner

ResearchAgent

SummaryAgent

PDFAgent

Determine whether RuntimeOrchestrator already owns this.

---

## 8.

Can the runtime already execute Executive Research?

If yes

Show the entry point.

If no

Explain why.

---

## 9.

What is the minimum change required so that the web application becomes only:

ResearchService

↓

AIAgentLabFacade

↓

RuntimeBootstrap

No duplicate orchestration.

No duplicate workflow.

---

# Repository Health Audit

Identify any duplicate implementations of:

WorkflowDefinition

TaskGraph

ExecutionPlan

TypedWorkflowContext

Workflow builders

Execution context

RuntimeResult

List each duplicate.

Recommend which implementation should remain.

---

# Deliverables

Produce a report.

Do not begin implementation until the report is complete.

The report must contain:

## Executive Summary

## Runtime Ownership Matrix

Example:

| Component | Owner | Evidence |
|-----------|-------|----------|

---

## Public Runtime APIs

List every runtime entry point.

---

## Missing Runtime Capabilities

List only genuine gaps.

Do not speculate.

---

## Duplicate Components

List duplicates.

Recommend removal.

---

## Integration Recommendation

Answer one question:

How should Executive Research integrate with AI Agent Lab using the smallest possible change?

---

## Proposed Changes

List only the minimum required changes.

No redesigns.

---

## Stop Conditions

If any required runtime capability is missing:

STOP.

Do not create a workaround.

Instead document:

- missing capability
- why it is missing
- minimum runtime change required

---

# Success Criteria

This sprint is complete only when:

- Runtime ownership is fully understood.
- No assumptions remain.
- Existing runtime APIs are identified.
- Duplicate implementations are identified.
- Minimum integration path is documented.
- No unnecessary code has been written.