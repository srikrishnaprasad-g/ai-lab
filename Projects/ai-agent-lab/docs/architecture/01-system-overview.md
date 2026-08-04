# AI Agent Lab - System Overview

## Vision

AI Agent Lab is a modular multi-agent AI platform designed to host multiple AI-powered applications.

The platform separates:

- User Experience
- Product Logic
- AI Orchestration
- Model Providers

This separation allows multiple applications to reuse the same AI runtime while remaining independently deployable.

---

## High-Level Architecture

                    +--------------------+
                    |   Web Frontend     |
                    |   (Next.js)        |
                    +---------+----------+
                              |
                              |
                              v
                    +--------------------+
                    | FastAPI Backend    |
                    | Product API Layer  |
                    +---------+----------+
                              |
                              |
                              v
                    +--------------------+
                    | Product Services   |
                    +---------+----------+
                              |
                              |
                              v
                    +--------------------+
                    | Research Engine    |
                    +---------+----------+
                              |
                              |
                              v
                    +--------------------+
                    | AI Agent Runtime   |
                    +---------+----------+
                              |
               +--------------+--------------+
               |                             |
               v                             v

        Gemini Provider              Future Providers

---

## Current Showcase Application

Executive Research

This application demonstrates:

- user input
- API communication
- AI orchestration
- structured report generation

Future showcase applications can reuse the same runtime.

---

## Design Principles

- Clean Architecture
- SOLID
- Separation of Concerns
- Reusable Runtime
- Provider Agnostic
- Stateless APIs
- Type Safety