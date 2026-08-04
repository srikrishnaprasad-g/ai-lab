# Phase 5.1 — End-to-End Browser Validation

## Sprint Type

**Product Validation Sprint**

This sprint is NOT an architecture sprint.

This sprint is NOT a refactoring sprint.

This sprint exists to prove that the existing Executive Research web application successfully invokes the existing AI Agent Lab runtime through the browser.

The goal is to achieve a complete end-to-end working MVP.

---

# Product Goal

A user should be able to:

1. Open the Executive Research web page.
2. Enter a research query.
3. Click **Generate Report**.
4. Wait while the existing AI Agent Lab runtime executes.
5. View:
   - Executive Summary
   - Key Findings
6. Click **Download PDF**.
7. Download the generated PDF successfully.

If these seven steps work, the sprint is successful.

---

# Important Principles

## Do NOT redesign anything.

Architecture is frozen.

Do NOT:

- redesign RuntimeBootstrap
- redesign RuntimeOrchestrator
- redesign Planner
- redesign Agents
- redesign FastAPI
- redesign React

Only fix issues preventing end-to-end execution.

---

## The CLI is the Source of Truth

`python cli.py`

already performs:

User Query

↓

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

↓

Report

The browser must execute exactly the same pipeline.

---

# Validation Tasks

## Backend

Start FastAPI.

Confirm:

- application starts
- dependencies resolve
- runtime initializes
- no import errors
- no runtime errors

---

## Frontend

Start Next.js.

Confirm:

- application loads
- Generate Report button works
- API call succeeds

---

## Runtime

Submit a real research query.

Confirm:

Planner executes.

↓

ResearchAgent executes.

↓

Tavily returns results.

↓

SummaryAgent invokes Gemini.

↓

PDFAgent generates report.

---

## API Response

Verify the backend returns:

```json
{
  "executive_summary": "...",
  "key_findings": [
    "...",
    "..."
  ],
  "pdf_url": "/reports/....pdf"
}
```

---

## Frontend

Verify:

Executive Summary renders.

Key Findings render.

Download PDF button becomes enabled.

---

## PDF

Click Download PDF.

Verify:

- File downloads successfully.
- File opens correctly.
- Generated content matches the browser output.

---

# Bug Fixes

Fix only bugs that prevent:

- runtime execution
- browser communication
- PDF generation
- PDF download

Do not perform unrelated refactoring.

---

# Repository Health

Remove:

- obsolete mock code
- dead code
- unused imports

Do not move folders.

Do not rename architecture.

---

# Documentation

Update:

apps/executive-research

- PROJECT_STATUS.md
- CHANGELOG.md

Document only actual completed work.

Do not mark the project as complete.

---

# Definition of Done

The sprint is complete only when the following user journey succeeds:

1. User opens the web page.
2. User enters a query.
3. Existing AI Agent Lab runtime executes.
4. Tavily searches the internet.
5. Gemini generates the executive summary.
6. PDF Agent generates the report.
7. Browser displays:
   - Executive Summary
   - Key Findings
8. User downloads the generated PDF.

No architecture changes should be introduced.

---

# Output

Provide:

1. Executive Summary
2. Bugs Found
3. Bugs Fixed
4. Files Modified
5. Validation Results
6. Remaining Blockers
7. Next Recommended Step