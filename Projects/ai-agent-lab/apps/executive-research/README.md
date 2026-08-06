# README.md

# Executive Research

> AI-powered executive research and report generation built on the AI Agent Lab runtime.

---

# Overview

Executive Research is a web application that transforms a natural language research request into an executive-ready report.

The application combines internet research, AI summarization, and automated report generation into a single workflow.

Users simply enter a research topic, and the system:

1. Searches the web for relevant information.
2. Summarizes the findings using Google Gemini.
3. Extracts key executive insights.
4. Generates a professionally formatted PDF report.
5. Returns both the on-screen summary and downloadable report.

The application is built as a showcase implementation on top of the AI Agent Lab runtime.

---

# Key Features

- Public web interface
- AI-powered executive summaries
- Internet research using Tavily
- Multi-agent workflow orchestration
- Downloadable PDF reports
- Responsive web interface
- Cloud deployment on Vercel and Render

---

# Technology Stack

## Frontend

- Next.js
- React
- TypeScript

## Backend

- FastAPI
- Python

## AI Runtime

- AI Agent Lab Runtime

## AI Services

- Tavily Search
- Google Gemini

## PDF

- ReportLab

---

# High-Level Architecture

```
Browser
   │
   ▼
Next.js Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
AI Agent Lab Runtime
   │
   ├── Tavily Search
   ├── Gemini Summary
   └── PDF Generation
```

---

# Production Deployment

Frontend

https://srikrishnaprasad-executive-summary.vercel.app

Backend

https://executive-research-api.onrender.com

API Documentation

https://executive-research-api.onrender.com/docs

---

# Local Development

Frontend

```bash
cd apps/executive-research/frontend
npm install
npm run dev
```

Backend

```bash
cd apps/executive-research/backend
uvicorn app.main:app --reload
```

---

# Documentation

See the `/docs` directory for:

- User Guide
- Deployment Guide
- Project Status
- Changelog
- Release Notes
- Architecture

---

# Roadmap

Upcoming improvements include:

- Persistent cloud storage
- Enhanced UI/UX
- Progress indicators
- Background processing
- Authentication
- Report history
- Analytics

---

# License

Refer to the root AI Agent Lab repository for licensing information.
