# ARCHITECTURE.md

# Executive Research – Technical Architecture

**Version:** v1.0.0  
**Last Updated:** August 2026

---

# Purpose

Executive Research is a reference application built on top of the AI Agent Lab runtime.

Its purpose is to demonstrate how a production web application can leverage the existing multi-agent runtime without duplicating orchestration logic.

The application is intentionally lightweight.

Business logic lives inside the AI Agent Lab runtime while the web application acts as a presentation and API layer.

---

# High-Level Architecture

```
                         User

                           │

                           ▼

                Next.js Frontend (Vercel)

                           │

                    REST API (HTTPS)

                           │

                           ▼

                FastAPI Backend (Render)

                           │

                           ▼

                 AIAgentLabFacade

                           │

                           ▼

                RuntimeBootstrap

                           │

                           ▼

              RuntimeOrchestrator

                           │

            WorkflowDefinition Execution

                           │

        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼

   Research Agent     Summary Agent      PDF Agent

        │                  │                  │

        ▼                  ▼                  ▼

     Tavily API       Gemini API       ReportLab

        │                  │                  │

        └──────────────┬───┴──────────────────┘

                       ▼

                 RuntimeResult

                       │

                       ▼

                 FastAPI Response

                       │

                       ▼

                 Next.js Frontend
```

---

# Design Principles

The architecture follows several guiding principles.

## 1. Single Runtime

Only one orchestration engine exists.

The web application does not construct or execute workflows independently.

---

## 2. Separation of Responsibilities

Frontend

- User interaction
- Progress updates
- Rendering results

Backend

- API endpoints
- Request validation
- Runtime invocation

Runtime

- Workflow execution
- Agent orchestration
- Context management

Agents

- Individual business capabilities

---

## 3. Reusable Runtime

The AI Agent Lab runtime is application-agnostic.

Executive Research is only one possible consumer.

Future applications may include:

- Resume Review
- Interview Coach
- Meeting Summarizer
- Product Strategy Assistant

All can reuse the same runtime.

---

# Workflow

## Step 1

User submits a research topic.

↓

## Step 2

Frontend sends a POST request.

↓

## Step 3

FastAPI validates the request.

↓

## Step 4

AIAgentLabFacade invokes the runtime.

↓

## Step 5

Runtime executes the workflow.

↓

Research Agent

↓

Summary Agent

↓

PDF Agent

↓

## Step 6

RuntimeResult returned.

↓

## Step 7

Frontend displays:

- Executive Summary
- Key Insights
- Download PDF

---

# AI Agents

## Research Agent

Responsibilities

- Search internet
- Retrieve relevant content
- Prepare research context

Provider

Tavily Search API

---

## Summary Agent

Responsibilities

- Analyze research
- Generate executive summary
- Extract key insights

Provider

Google Gemini

---

## PDF Agent

Responsibilities

- Generate formatted PDF
- Save report
- Return download path

Technology

ReportLab

---

# Deployment Architecture

Frontend

Vercel

↓

Backend

Render

↓

External APIs

- Tavily
- Gemini

---

# Current Limitations

- PDFs stored on local Render filesystem
- No authentication
- No persistent report history
- Limited timeout recovery

---

# Future Evolution

Planned architectural improvements:

- Workflow Registry
- Background workers
- Cloud object storage
- Streaming responses
- Event-based execution
- Observability and monitoring

---

# Architectural Decision

The Executive Research application deliberately avoids implementing its own workflow orchestration.

All orchestration responsibilities remain within the AI Agent Lab runtime.

This ensures consistency, maintainability, and enables future applications to share the same execution engine without code duplication.
