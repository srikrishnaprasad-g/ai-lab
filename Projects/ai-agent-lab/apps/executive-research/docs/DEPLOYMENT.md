# DEPLOYMENT.md

# Executive Research – Deployment Guide

**Version:** v1.0.0 Public Beta  
**Last Updated:** August 2026

---

# 1. Overview

Executive Research is deployed as a cloud-native web application using a split frontend/backend architecture.

| Component | Platform |
|-----------|----------|
| Frontend | Vercel |
| Backend API | Render |
| Source Code | GitHub |
| Search Provider | Tavily |
| LLM Provider | Google Gemini |
| PDF Generation | ReportLab |

---

# 2. Production Architecture

```
                         User
                           │
                           ▼
                 Vercel (Next.js Frontend)
                           │
                           ▼
             FastAPI Backend (Render)
                           │
                           ▼
                  AI Agent Lab Runtime
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
   Tavily Search                     Gemini Summary
        │                                     │
        └──────────────┬──────────────────────┘
                       ▼
                 PDF Generation
                       │
                       ▼
              JSON Response + PDF
                       │
                       ▼
                     Browser
```

---

# 3. Production URLs

## Frontend

https://srikrishnaprasad-executive-summary.vercel.app

## Backend API

https://executive-research-api.onrender.com

## API Documentation

https://executive-research-api.onrender.com/docs

---

# 4. Deployment Workflow

## Backend

Platform:
Render

Root Directory:

Projects/ai-agent-lab/apps/executive-research/backend

Build Command

```
pip install -r requirements.txt
pip install -e ../../../..
```

Start Command

```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## Frontend

Platform:
Vercel

Root Directory

```
Projects/ai-agent-lab/apps/executive-research/frontend
```

Framework

```
Next.js
```

Build Command

```
npm run build
```

---

# 5. Required Environment Variables

## Backend (Render)

```
GEMINI_API_KEY
TAVILY_API_KEY
CORS_ORIGINS
REPORTS_DIR
```

---

## Frontend (Vercel)

```
NEXT_PUBLIC_API_BASE_URL
```

Example

```
NEXT_PUBLIC_API_BASE_URL=https://executive-research-api.onrender.com
```

---

# 6. Deployment Lessons Learned

## CORS Origins

**Important**

Do **NOT** include a trailing slash.

Correct

```
https://srikrishnaprasad-executive-summary.vercel.app
```

Incorrect

```
https://srikrishnaprasad-executive-summary.vercel.app/
```

A trailing slash causes browser preflight requests (OPTIONS) to fail with HTTP 400.

---

## Root Directory

Both Render and Vercel must point to the Executive Research application rather than the repository root.

---

## Production Build

Always validate locally before deployment.

Frontend

```
npm run build
```

Backend

```
uvicorn app.main:app --reload
```

---

# 7. Known Production Limitations

- PDF reports are stored on Render's local filesystem.
- Generated reports are not persistent across service redeployments.
- Long-running Gemini requests may occasionally time out.
- Authentication is not implemented in v1.0.

---

# 8. Future Improvements

- Cloud object storage (Amazon S3 / Cloudflare R2)
- Background job processing
- Streaming progress updates
- User authentication
- Persistent report history
- Custom domains
- Monitoring and alerting

---

# 9. Deployment Checklist

Before each production deployment:

- Backend builds successfully
- Frontend builds successfully
- Environment variables verified
- CORS origins updated
- Production URLs verified
- End-to-end research flow tested
- PDF download verified
