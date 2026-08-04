# Sprint 4.4 – Platform Integration Layer

## Role

You are a Principal Software Architect.

Your goal is to prepare Executive Research for integration with AI Agent Lab without implementing any AI functionality.

This sprint establishes clean architectural boundaries between the product and the AI platform.

---

# Mandatory Preparation

Read:

- docs/product/EXECUTIVE_RESEARCH_PRD.md
- docs/product/UI_SPECIFICATION.md

Review:

- frontend architecture
- backend architecture
- service layer

Do not change frontend functionality.

---

# Objective

Introduce a Platform Integration Layer.

The backend must no longer assume that ResearchService owns report generation.

Instead:

ResearchService

↓

ResearchEngine

↓

Runtime Interface

---

# Folder Structure

Create

app/

    engine/

        research_engine.py

        runtime.py

    core/

        responses.py

        exceptions.py

        request_context.py

---

# Runtime Interface

Create

runtime.py

Define an abstract interface.

Example

class RuntimeInterface:

    async def generate_report(query: str):
        ...

Do NOT implement AI logic.

Create a placeholder implementation.

Return mocked data.

---

# ResearchEngine

Move report orchestration here.

Responsibilities:

- receive query

- call runtime

- return domain object

No HTTP logic.

No FastAPI dependencies.

---

# ResearchService

ResearchService should now only

- validate business request

- call ResearchEngine

- return result

No mocked data should remain here.

---

# API Response Models

Create reusable models

ApiResponse[T]

ErrorResponse

Use these across endpoints.

---

# Request Context

Create

request_context.py

Generate

- request_id

- timestamp

Make request ID available for logging.

---

# Logging

Log

Request received

↓

ResearchService

↓

ResearchEngine

↓

Runtime

↓

Response completed

Use request_id throughout.

---

# Exception Hierarchy

Create

BaseApplicationException

ValidationException

RuntimeException

Map them to HTTP responses.

---

# Dependency Injection

Prepare constructors so future Runtime implementations can be injected.

Avoid global singletons.

---

# Validation

Run

python -m compileall .

Verify

POST /api/v1/research

still returns mocked data.

Frontend should require no changes.

---

# Code Quality

Follow

- SOLID

- SRP

- Dependency Injection

- Clean Architecture

- Strict typing

---

# Stop Conditions

Do NOT

- integrate Gemini

- integrate AI Agent Lab

- generate PDFs

- redesign frontend

- modify API contract

Only establish the integration architecture.

---

# Implementation Report

Provide

1. Files Created

2. Files Modified

3. Validation

4. Architectural Decisions

5. Remaining Work