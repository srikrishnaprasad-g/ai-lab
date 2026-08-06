# USER_GUIDE.md

# Executive Research User Guide

## Overview

Executive Research is an AI-powered web application that transforms a natural language research request into an executive-ready report.

Instead of manually searching the web, reading dozens of articles, and creating presentation material, users simply enter a research topic. The application performs the research automatically and produces a concise executive summary together with a downloadable PDF report.

---

# What Can This Application Do?

The application can:

- Search the internet for recent information
- Analyze and summarize findings using AI
- Identify key business insights
- Generate an executive-ready report
- Download a professionally formatted PDF

---

# Typical Workflow

```
Enter Research Topic

↓

Internet Search

↓

Research Analysis

↓

Executive Summary

↓

Key Insights

↓

Generate PDF

↓

Download Report
```

---

# Example Queries

- Future of AI Agents
- Healthcare AI Trends
- Electric Vehicle Market
- Global Semiconductor Industry
- Climate Change Impact on Agriculture
- Competitor Analysis for Salesforce
- Generative AI in Banking

---

# Technology Stack

Frontend

- Next.js
- React
- TypeScript

Backend

- FastAPI
- Python

AI Runtime

- AI Agent Lab Runtime

External Services

- Tavily Search API
- Google Gemini

Document Generation

- ReportLab

Deployment

- Vercel
- Render

---

# How It Works

The application orchestrates multiple AI agents.

## Research Agent

Searches the web using Tavily.

---

## Summary Agent

Uses Google Gemini to analyze search results and generate an executive summary.

---

## PDF Agent

Creates a professionally formatted PDF report.

---

# Current Capabilities

✔ Public cloud deployment

✔ Real-time internet search

✔ AI-generated executive summaries

✔ Key insight extraction

✔ PDF generation

✔ Downloadable reports

---

# Current Limitations

- Reports are not permanently stored.
- Very large research topics may require additional processing time.
- AI responses depend on the availability of external services.

---

# Intended Audience

Executive Research is designed for:

- Product Managers
- Business Leaders
- Strategy Teams
- Consultants
- Analysts
- Students
- Researchers

---

# Future Roadmap

Future releases will include:

- Report history
- Multiple report templates
- Rich visualizations
- Charts and graphs
- Multi-language support
- Authentication
- Team collaboration
- Persistent cloud storage
