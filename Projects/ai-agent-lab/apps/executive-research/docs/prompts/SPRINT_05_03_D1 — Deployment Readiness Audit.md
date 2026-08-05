# Sprint D1 — Deployment Readiness Audit

## Objective

Prepare the Executive Research application for production deployment.

Do NOT deploy yet.

This sprint is an audit only.

---

# Goal

Determine whether the application is ready to deploy to:

Frontend:
- Vercel

Backend:
- Render

---

# Review

Inspect:

- frontend
- backend
- runtime
- pyproject.toml
- requirements.txt
- package.json
- environment variables
- report generation
- startup commands

---

# Verify

## Backend

Identify:

- Build command
- Start command
- Python version
- Required environment variables
- Working directory
- Port handling

Confirm that Render can deploy the backend.

---

## Frontend

Identify:

- Build command
- Output type
- Environment variables
- API URL configuration

Confirm that Vercel can deploy the frontend.

---

## Runtime

Confirm that the deployed backend will include:

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

No local dependencies should remain.

---

## Reports

Verify that PDF generation works on Render.

If local filesystem storage is unsuitable for production, recommend the smallest acceptable alternative.

Do not implement changes yet.

---

# Deliverables

Provide:

1. Deployment readiness score.
2. Missing configuration.
3. Required environment variables.
4. Render configuration.
5. Vercel configuration.
6. Startup commands.
7. Build commands.
8. Any deployment blockers.

Do not refactor unrelated code.
Do not deploy.