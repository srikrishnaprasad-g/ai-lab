# Sprint 4.2 – Research API & Service Layer

## Role

You are a Senior Backend Engineer.

Your objective is to establish the backend service architecture for Executive Research.

Do NOT integrate AI Agent Lab yet.

Do NOT call any LLM.

The endpoint should return mocked data while following production architecture.

---

# Mandatory Preparation

Read

```
docs/product/EXECUTIVE_RESEARCH_PRD.md
```

Read

```
docs/product/UI_SPECIFICATION.md
```

Review

```
apps/executive-research/backend
```

Understand the existing backend structure before making changes.

---

# Objective

Create a proper API layer.

The frontend should eventually call

```
POST /api/v1/research
```

The implementation must use

```
Router

↓

Service

↓

Mock Response
```

No business logic should exist inside API routers.

---

# Folder Structure

Use

```
app/

    api/

        router.py

        v1/

            health.py

            research.py

    services/

        research_service.py

    schemas/

        research.py

    models/

    core/

    config/
```

---

# API Router

Move

```
/health
```

into

```
health.py
```

Create

```
research.py
```

using

```
APIRouter
```

The router should only

- validate requests
- call ResearchService
- return responses

---

# Research Service

Create

```
services/research_service.py
```

The service should expose

```python
generate_report(query: str)
```

The service should currently return mocked data.

Do not call AI Agent Lab.

---

# Response Format

Return

```json
{
  "status": "success",
  "data": {
    "executive_summary": "...",
    "key_insights": [
      "...",
      "..."
    ],
    "report_id": "uuid"
  }
}
```

Generate a UUID for every request.

---

# Request Validation

Reject

- empty queries
- whitespace-only queries
- queries longer than 5000 characters

Return proper HTTP status codes.

---

# Error Handling

Use FastAPI exception handlers.

Return consistent JSON

```
{
    "status":"error",
    "message":"..."
}
```

---

# Main Application

main.py should become extremely small.

Its responsibilities are only

- create app
- load config
- include routers
- configure middleware

Nothing else.

---

# Documentation

Update

```
PROJECT_STATUS.md
```

Include

Sprint 4.2 completion.

---

# Validation

Run

```
python -m compileall .
```

Run

```
uvicorn app.main:app --reload
```

Verify

Swagger

```
/docs
```

Verify

```
POST /api/v1/research
```

Verify

```
GET /health
```

---

# Code Quality

Follow

- SOLID
- SRP
- strict typing
- dependency injection where appropriate
- no duplicated logic

---

# Stop Conditions

Do NOT implement

- Gemini

- OpenAI

- Claude

- Groq

- AI Agent Lab runtime

- PDF generation

- frontend changes

Only establish the service architecture.

---

# Implementation Report

Provide

1. Files Created

2. Files Modified

3. Commands Executed

4. Validation Performed

5. Assumptions

6. Remaining Work