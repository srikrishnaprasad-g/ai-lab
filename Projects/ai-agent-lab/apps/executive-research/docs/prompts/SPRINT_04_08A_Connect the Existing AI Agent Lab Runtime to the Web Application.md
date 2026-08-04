# Sprint 4.8 — Connect the Existing AI Agent Lab Runtime to the Web Application

## Sprint Type

**Implementation Sprint (MVP Delivery)**

This sprint is focused on delivering a working Executive Research web application.

The architecture has been finalized.

Do NOT redesign the runtime.

Do NOT introduce new abstractions.

Do NOT refactor the runtime.

Your only objective is to make the existing working AI Agent Lab pipeline accessible through the existing web application.

---

# Product Goal

A user should be able to:

1. Open the Executive Research web page.
2. Enter a research query.
3. Click **Generate Report**.
4. The existing AI Agent Lab runtime should execute.
5. The web page should display:
   - Executive Summary
   - Key Findings
6. A generated PDF should be available for download.
7. Clicking **Download PDF** should download the generated report to the user's local machine.

Nothing more.

---

# Existing Reference Implementation

The current CLI implementation is the source of truth.

```
python cli.py
```

already performs the complete workflow:

User Query

↓

Planner

↓

Research Agent

↓

Tavily Search

↓

Summary Agent

↓

Gemini

↓

PDF Agent

↓

Generated Report

Do NOT recreate this workflow.

Do NOT duplicate this workflow.

The web application must invoke exactly the same execution path.

---

# Mandatory Preparation

Before writing code:

Before making changes:

Read

apps/executive-research/docs/product/EXECUTIVE_RESEARCH_PRD.md
apps/executive-research/docs/product/UI_SPECIFICATION.md
apps/executive-research/PROJECT_STATUS.md

Review:

- cli.py
- RuntimeBootstrap
- RuntimeOrchestrator
- Planner
- ResearchAgent
- SummaryAgent
- PDFAgent

Determine exactly how `cli.py` starts the runtime.

Use that execution path.

Review the Executive Research frontend and Backend implementation under the path apps/executive-research/

---

# Primary Objective

Replace any temporary or mock execution inside the FastAPI backend.

The backend must invoke the same runtime that `cli.py` invokes.

There must be only ONE implementation of the research pipeline.

The CLI and the web application must share the same runtime.

---

# Required Work

## Step 1

Inspect `cli.py`.

Identify:

- entry function
- runtime bootstrap
- runtime execution call
- runtime result

Do not modify behaviour.

---

## Step 2

Modify:

```
AIAgentLabFacade
```

so that it simply invokes the same runtime used by `cli.py`.

Do NOT:

- build TaskGraph
- create WorkflowDefinition
- orchestrate agents
- invoke providers directly

Those already exist.

---

## Step 3

FastAPI Endpoint

Keep

```
POST /api/v1/research
```

unchanged.

The endpoint should simply call:

```
ResearchService

↓

AIAgentLabFacade

↓

Existing Runtime
```

---

## Step 4

Return:

```json
{
  "executive_summary": "...",
  "key_findings": [
    "...",
    "..."
  ],
  "pdf_url": "/reports/generated-report.pdf"
}
```

The response contract must remain unchanged.

---

## Step 5

PDF Download

Expose a FastAPI endpoint that returns the generated PDF.

Use FastAPI FileResponse.

The browser should download the generated PDF directly.

---

## Step 6

Frontend

No redesign.

Reuse the existing UI.

After pressing Generate Report:

Display:

- Executive Summary
- Key Findings

Enable:

Download PDF

No additional UI work is required.

---

# Constraints

Do NOT:

- redesign RuntimeBootstrap
- redesign RuntimeOrchestrator
- redesign Planner
- redesign BaseAgent
- redesign SearchProvider
- redesign Gemini provider
- redesign PDF generation
- redesign PromptBuilder
- redesign runtime models
- introduce WorkflowRegistry
- introduce WorkflowFactory
- introduce new architecture

Reuse the existing implementation.

---

# Validation

Verify locally.

## Backend

```
uvicorn app.main:app --reload
```

Backend starts successfully.

---

## Frontend

```
npm run dev
```

Frontend starts successfully.

---

## Browser

Open:

```
http://localhost:3000
```

---

## Execute

Enter a research query.

Verify the existing runtime executes.

Expected execution:

Planner

↓

Research Agent

↓

Tavily

↓

Summary Agent

↓

Gemini

↓

PDF Agent

---

## Verify Response

The browser should display:

- Executive Summary
- Key Findings

---

## Verify PDF

Click:

Download PDF

Expected:

Browser downloads the generated report.

---

# Repository Health

Before completing:

- Remove obsolete mock code.
- Remove unused imports.
- Remove dead code.
- Remove duplicate runtime execution paths.

Do NOT remove reusable runtime components.

---

# Documentation

Update:

apps/executive-research

- PROJECT_STATUS.md
- CHANGELOG.md

Document:

- Web application now executes the existing AI Agent Lab runtime.
- CLI and Web share the same execution pipeline.
- No runtime duplication exists.

Do NOT mark the project as complete.

---

# Definition of Done

The sprint is complete only when:

- `cli.py` remains fully functional.
- The web application invokes the same runtime as `cli.py`.
- No duplicate orchestration exists.
- The browser displays:
  - Executive Summary
  - Key Findings
- PDF generation succeeds.
- Download PDF downloads the generated report.
- The React UI remains unchanged.
- The FastAPI API contract remains unchanged.
- Repository health passes.

---

# Stop Conditions

Stop immediately and provide an investigation report if:

- The web application cannot invoke the same runtime as `cli.py`.
- RuntimeBootstrap lacks a suitable public entry point.
- Existing runtime components require redesign.
- A second orchestration layer becomes necessary.
- Existing functionality would need to be duplicated.

Do NOT invent a workaround.

---

# Implementation Report

Provide:

1. Executive Summary
2. CLI Execution Path Identified
3. Runtime Entry Point Used
4. Files Modified
5. Files Removed
6. End-to-End Validation Results
7. Repository Health Findings
8. Documentation Updated
9. Remaining Work
10. Any blockers encountered