# Sprint D1 (Revised) — Executive Research Deployment Readiness Audit

## Context

This is NOT an audit of the Product Portfolio project.

Audit ONLY the Executive Research application located at:

```
apps/executive-research/
```

This application is already functionally complete and works locally.

Verified working functionality:

- Next.js frontend loads successfully.
- FastAPI backend starts successfully.
- User enters a research query.
- FastAPI invokes the existing AI Agent Lab Runtime.
- Tavily performs the web search.
- Research Agent processes the results.
- Summary Agent uses Gemini to generate:
  - Executive Summary
  - Key Insights
- PDF Agent generates the Executive Report.
- The frontend displays:
  - Executive Summary
  - Key Insights
- Download Executive Report successfully downloads the generated PDF.

This entire end-to-end flow has already been verified locally.

The objective of this sprint is NOT to redesign or rebuild anything.

The objective is ONLY to determine what is required to deploy the existing working application to production.

---

# Deployment Target Architecture

Frontend

Vercel

↓

HTTPS

↓

Backend

Render

↓

Existing AI Agent Lab Runtime

↓

Tavily

↓

Gemini

↓

PDF Generation

↓

Response returned to browser

No local laptop should be required after deployment.

---

# Objective

Perform a deployment readiness audit of ONLY the Executive Research application.

Do NOT inspect the Product Portfolio project.

Do NOT inspect unrelated AI Agent Lab components unless they are direct runtime dependencies of Executive Research.

---

# Audit Scope

## Backend

Audit:

```
apps/executive-research/backend
```

Verify:

- FastAPI entry point
- Startup command
- Working directory
- Runtime integration
- Python dependencies
- pyproject.toml
- requirements.txt
- Editable package installation
- Port configuration
- Health endpoint
- Research endpoint
- Download endpoint

Determine the exact Render deployment configuration.

---

## Frontend

Audit:

```
apps/executive-research/frontend
```

Verify:

- package.json
- Build command
- Output mode
- API configuration
- Environment variables
- Production build
- Static assets

Determine the exact Vercel deployment configuration.

---

## Runtime

Verify that the deployed backend includes the existing runtime.

Confirm that the deployed application executes:

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

RuntimeResult

No local dependencies should remain.

---

## Environment Variables

Identify every required environment variable.

Examples:

- GEMINI_API_KEY
- TAVILY_API_KEY
- REPORTS_DIR
- NEXT_PUBLIC_API_URL

Also identify any unnecessary variables that can be removed.

---

## File Storage

Review PDF generation.

Determine whether the current local filesystem approach is acceptable for the MVP deployment.

If not,

recommend the SMALLEST production-ready improvement.

Do NOT implement cloud storage unless absolutely necessary.

The priority is to ship the MVP.

---

## Production Checklist

Verify:

✓ Backend can build on Render

✓ Backend can start on Render

✓ Frontend can build on Vercel

✓ Frontend can communicate with Render

✓ Runtime executes correctly

✓ PDF generation works

✓ PDF download works

✓ No localhost references remain

✓ No hardcoded paths remain

✓ No development-only configuration remains

---

# Constraints

Do NOT:

- redesign architecture
- move folders
- rename components
- introduce new abstractions
- migrate frameworks
- rebuild the runtime

Only identify deployment blockers.

If a blocker exists,

recommend the SMALLEST possible fix.

---

# Deliverables

Provide:

## 1. Deployment Readiness Score

Rate ONLY the Executive Research application.

Not the portfolio project.

---

## 2. Render Configuration

Provide:

- Root directory
- Build command
- Start command
- Python version
- Required environment variables

---

## 3. Vercel Configuration

Provide:

- Root directory
- Build command
- Output configuration
- Environment variables

---

## 4. Remaining Deployment Blockers

List ONLY genuine deployment blockers.

Ignore optional future improvements.

---

## 5. Recommended Fixes

For each blocker provide:

- Root cause
- Recommended fix
- Estimated effort

---

## 6. Final Verdict

Choose one:

✅ Ready to Deploy

⚠ Minor Fixes Before Deployment

❌ Not Ready

Justify the decision using only the Executive Research application.