# Sprint 4.3 – Frontend ↔ Backend Integration

## Role

You are a Senior Full Stack Engineer.

Your objective is to connect the Executive Research frontend to the FastAPI backend.

The backend already exposes

POST /api/v1/research

Do NOT modify backend functionality.

Do NOT integrate AI Agent Lab.

Only replace the frontend mock service with a real HTTP client.

---

# Mandatory Preparation

Read

docs/product/EXECUTIVE_RESEARCH_PRD.md

Read

docs/product/UI_SPECIFICATION.md

Review

apps/executive-research/frontend

Review

apps/executive-research/backend

Understand the existing architecture before making changes.

---

# Objective

Replace

services/mockResearchService.ts

with

services/api/researchApi.ts

The user experience must remain unchanged.

The frontend should now communicate with FastAPI instead of mocked data.

---

# Folder Structure

Create

src/

    services/

        api/

            researchApi.ts

        mock/

            mockResearchService.ts

Move the current mock service into

```
mock/
```

without deleting it.

---

# API Client

Create

```
researchApi.ts
```

Expose

```ts
generateResearchReport(query: string)
```

Use

```
fetch()
```

Do not introduce Axios.

---

# Backend URL

Create

```
src/config/api.ts
```

Example

```ts
export const API_BASE_URL =
    process.env.NEXT_PUBLIC_API_BASE_URL ??
    "http://localhost:8000";
```

Do NOT hardcode URLs inside services.

---

# Service

The service should call

```
POST

/api/v1/research
```

Send

```json
{
    "query": "..."
}
```

Parse

```json
{
    "status":"success",
    "data":{...}
}
```

Return only

```
data
```

to the UI.

---

# Hook

Modify

```
useExecutiveResearch.ts
```

Replace

```ts
generateMockResearchReport(...)
```

with

```ts
generateResearchReport(...)
```

No other business logic should change.

---

# Error Handling

Handle

- network failures

- timeout

- backend errors

Return friendly messages.

Do not expose raw exceptions.

---

# Loading

Preserve existing loading behaviour.

Do not change UX.

---

# Environment Variables

Create

```
.env.local
```

Example

```
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

---

# Validation

Start backend

```
uvicorn app.main:app --reload
```

Start frontend

```
npm run dev
```

Verify

End-to-end flow

User submits query

↓

POST request succeeds

↓

Response rendered

Verify browser console

No errors

Verify Network tab

Status 200

---

# Code Quality

Follow

- SOLID

- SRP

- Strict TypeScript

- No duplicated logic

- No unnecessary dependencies

---

# Stop Conditions

Do NOT

- modify backend APIs

- integrate Gemini

- integrate AI Agent Lab

- generate PDFs

- redesign UI

Only integrate the frontend with the existing backend.

---

# Implementation Report

Provide

1. Files Created

2. Files Modified

3. Validation Performed

4. Assumptions

5. Remaining Work