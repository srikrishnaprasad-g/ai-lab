Please use the file:

./executive-research-ui-redesign.zip

Follow the instructions below...

# Sprint 6.0 – Executive Research UI/UX Refresh (Frontend Only)

## Background

The Executive Research application has reached **v1.0.0 Public Beta**.

The application is fully functional and publicly deployed.

Current architecture:

User
↓

Next.js Frontend

↓

FastAPI Backend

↓

AI Agent Lab Runtime

↓

Research Agent (Tavily)

↓

Summary Agent (Gemini)

↓

PDF Agent

↓

Frontend displays:

- Executive Summary
- Key Findings
- Download PDF

The end-to-end workflow is already working correctly both locally and in production.

This sprint is **purely a UI/UX improvement sprint**.

---

## Goal

Replace the existing frontend UI with the redesigned UI contained in the supplied ZIP archive while preserving **all existing functionality**.

---

## Source Files

The ZIP contains the redesigned frontend.

Copy ONLY the files under:

executive-research-ui-redesign/frontend/src/

into

Projects/ai-agent-lab/apps/executive-research/frontend/src/

overwriting the existing frontend files.

Do NOT modify anything outside the frontend/src directory unless absolutely required to resolve build issues.

---

## Important Constraints

Do NOT modify:

- backend/
- runtime/
- providers/
- agents/
- workflow/
- API contracts
- FastAPI routes
- request/response models
- deployment configuration
- environment variables

Do NOT change:

- research API
- PDF generation
- Runtime integration
- Download endpoint

These are already production validated.

---

## Preserve Existing Behaviour

After the redesign the application must still support:

✅ User enters a research query

↓

✅ FastAPI backend receives request

↓

✅ AI Agent Lab Runtime executes

↓

✅ Tavily searches the internet

↓

✅ Gemini produces Executive Summary

↓

✅ PDF Agent generates report

↓

✅ Executive Summary displayed

↓

✅ Key Findings displayed

↓

✅ Download PDF works

No functionality regression is acceptable.

---

## Build Validation

After copying the files:

Navigate to:

Projects/ai-agent-lab/apps/executive-research/frontend

Run:

npm install

Then

npm run build

Fix any TypeScript or React issues introduced by the redesign.

Do NOT introduce backend changes.

---

## Local Validation

Run

npm run dev

Verify:

✓ Home page loads

✓ New UI renders correctly

✓ Query textbox works

✓ Progress tracker works

✓ Executive Summary displays

✓ Key Findings display

✓ Download PDF button still downloads the generated report

Verify the frontend communicates correctly with the existing backend running locally.

---

## Deliverables

Provide:

1. Files modified
2. Any fixes required after merging
3. Build output
4. Local validation summary
5. `git diff --stat`

Do NOT commit.

Do NOT push.

Do NOT deploy.

Stop after local validation and wait for my review.