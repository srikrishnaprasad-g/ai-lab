# Sprint 4.7 — Executive Research Runtime Integration

## Sprint Type

**Integration Sprint**

This is **NOT** a feature sprint and **NOT** an architecture redesign sprint.

The objective is to replace the temporary web-specific orchestration with the existing AI Agent Lab runtime while keeping the public API and React frontend unchanged.

---

# Role

You are the Lead Software Engineer for AI Agent Lab.

Your responsibility is to integrate the Executive Research web application with the existing AI Agent Lab runtime.

You must preserve all established architecture, engineering standards, and ADRs.

---

# Mandatory Preparation

Before making any code changes, read the following documents completely:

- PROJECT.md
- ENGINEERING.md
- DECISIONS.md
- PROJECT_STATUS.md
- CHANGELOG.md
- README.md

Review the existing runtime implementation before writing any code.

---

# Critical Architectural Rules

## Rule 1 — Reuse Before Create

If an existing AI Agent Lab component already provides the required functionality, **reuse it**.

Do **NOT** create a replacement.

New classes should only be introduced when no suitable existing implementation exists.

---

## Rule 2 — Architecture Freeze

This sprint is an integration sprint.

Do NOT redesign:

- RuntimeBootstrap
- RuntimeOrchestrator
- Planner
- BaseAgent
- Provider abstractions
- Prompt framework
- Search framework
- PDF framework
- Runtime contracts

Reuse them exactly as designed.

---

## Rule 3 — Runtime Owns Orchestration

The web application must never orchestrate agents.

Only RuntimeOrchestrator is allowed to coordinate:

Planner

↓

ResearchAgent

↓

SummaryAgent

↓

PDFAgent

---

## Rule 4 — Thin Application Layer

Executive Research is a web application built **on top of** AI Agent Lab.

Business logic belongs inside AI Agent Lab.

The web application should only:

- accept requests
- invoke the runtime
- return responses

---

# Sprint Objective

Replace the temporary backend orchestration with the existing AI Agent Lab runtime.

Target architecture:

```text
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

LLM Provider (Gemini)

↓

PDFAgent

↓

RuntimeResult

↓

ResearchResponse

↓

React UI
```

---

# Existing Runtime Components

The runtime already provides:

- RuntimeBootstrap
- RuntimeOrchestrator
- Planner
- ResearchAgent
- SummaryAgent
- PDFAgent
- SearchProvider abstraction
- Tavily implementation
- LLMProvider abstraction
- Gemini provider
- PromptBuilder
- PDF generation
- RuntimeResult

Reuse all of them.

Do not duplicate functionality.

---

# Scope

## 1. Remove Duplicate Web Orchestration

Remove the following components **only if they become unused**:

- ExecutiveResearchWorkflow
- WorkflowEngine
- MockAgentRuntime

Remove all unused imports, registrations, and dead code.

Do **NOT** remove reusable AI Agent Lab runtime components.

---

## 2. Create AIAgentLabFacade

Create:

```text
apps/executive-research/backend/integration/

    ai_agent_lab.py
```

Responsibilities:

- Accept research query
- Invoke RuntimeBootstrap
- Wait for runtime completion
- Convert RuntimeResult into API response
- Return normalized data

The facade is the **only** integration point between the web application and AI Agent Lab.

---

## 3. ResearchService

ResearchService should only:

- validate request
- call AIAgentLabFacade
- return response

ResearchService must NEVER:

- instantiate runtime objects
- orchestrate agents
- call providers directly
- contain business logic

---

## 4. Dependency Injection

Update dependencies.py so that construction becomes:

```text
RuntimeBootstrap

↓

AIAgentLabFacade

↓

ResearchService
```

No runtime object should be instantiated inside API routes.

---

## 5. API Layer

Keep the existing API unchanged.

Endpoint:

```text
POST /api/v1/research
```

Request schema must remain unchanged.

Response contract must remain unchanged:

```json
{
  "executive_summary": "...",
  "key_findings": [
    "...",
    "..."
  ],
  "pdf_url": "/reports/report.pdf"
}
```

No frontend changes should be required.

---

# Runtime Integration

The facade must invoke the existing runtime.

The runtime must execute:

Planner

↓

ResearchAgent

↓

Search Provider

↓

SummaryAgent

↓

PDFAgent

The web application must NEVER invoke these agents individually.

---

# Search Integration

ResearchAgent must use the existing SearchProvider abstraction.

Current provider:

- Tavily

No search logic should exist inside the web application.

---

# Summary Integration

SummaryAgent must reuse:

- PromptBuilder
- Gemini provider
- Response validation
- Existing prompt templates

Do not create duplicate prompts unless absolutely necessary.

---

# PDF Integration

PDFAgent must generate the existing PDF report.

Return:

- generated PDF path
- download URL

Expose a FastAPI FileResponse endpoint.

Clicking **Download PDF** in the UI must download the generated PDF directly to the user's local machine.

---

# Folder Structure

Target backend structure:

```text
backend/

├── api/
├── integration/
│      ai_agent_lab.py
├── schemas/
├── services/
└── dependencies.py
```

Remove obsolete workflow folders only if they become unused.

Do not modify the AI Agent Lab runtime folder structure.

---

# End-to-End Validation

The following flow **must** work:

```text
User enters query

↓

POST /api/v1/research

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

Tavily Search

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

React UI

↓

Download PDF
```

---

# Validation Checklist

## Backend

- Project compiles
- Imports resolve
- Dependency injection works
- No duplicate orchestration remains

---

## Runtime

Verify execution order:

Planner

↓

ResearchAgent

↓

Tavily

↓

SummaryAgent

↓

Gemini

↓

PDFAgent

---

## API

POST:

```text
/api/v1/research
```

returns:

- Executive Summary
- Key Findings
- PDF URL

---

## Frontend

User can:

- Enter a query
- Submit
- Wait for execution
- View Executive Summary
- View Key Findings
- Click Download PDF
- Download the generated PDF

---

# Repository Health

Before completing the sprint:

- Remove dead code
- Remove obsolete imports
- Remove duplicate orchestration
- Remove unused files
- Validate folder structure
- Ensure documentation reflects implementation

---

# Documentation Updates

Update:

- PROJECT_STATUS.md
- CHANGELOG.md

Document:

- Runtime integration completed
- Duplicate orchestration removed
- Executive Research now uses AI Agent Lab runtime
- No public API changes

---

# Definition of Done

The sprint is complete only when:

- Executive Research uses the existing AI Agent Lab runtime.
- No duplicate orchestration exists.
- RuntimeBootstrap is the only runtime entry point.
- RuntimeOrchestrator owns orchestration.
- Planner executes normally.
- ResearchAgent performs Tavily search.
- SummaryAgent generates executive summary and key findings using Gemini.
- PDFAgent generates the report.
- FastAPI returns:
  - executive_summary
  - key_findings
  - pdf_url
- React UI works without modification.
- Download PDF downloads the generated report locally.
- Repository health passes.
- Documentation is updated.

---

# Stop Conditions

Stop immediately and produce an investigation report if any of the following occur:

- A new orchestration layer appears.
- Existing runtime components require redesign.
- Runtime contracts need breaking changes.
- AI Agent Lab architecture must be modified to support the web application.
- API contract changes.
- React UI changes become necessary.
- Existing runtime functionality is duplicated.

Do **NOT** continue implementation until the root cause is identified.

---

# Implementation Report

At the end of the sprint, provide:

1. Executive Summary
2. Files Created
3. Files Modified
4. Files Removed
5. Integration Flow
6. Validation Results
7. Repository Health Findings
8. Documentation Updated
9. Remaining Technical Debt
10. Recommendations (if any)