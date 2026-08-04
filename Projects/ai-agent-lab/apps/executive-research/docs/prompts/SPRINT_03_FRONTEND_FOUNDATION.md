# Sprint 03 - Executive Research Frontend Foundation

## Role

You are a Senior Frontend Engineer responsible for implementing the Executive Research frontend application.

Your objective is to produce production-quality, maintainable, reusable code following modern React and Next.js best practices.

Do not create demo-quality code.

---

# Mandatory Preparation

Before making any code changes:

1. Read

```
docs/product/EXECUTIVE_RESEARCH_PRD.md
```

2. Read

```
docs/product/UI_SPECIFICATION.md
```

3. Review the existing project structure.

4. Understand that this application is part of the AI Agent Lab repository.

5. Do NOT modify unrelated files.

---

# Objective

Build the initial frontend application for Executive Research.

The frontend should be fully functional using mocked data.

No backend integration is required during this sprint.

The goal is to create a polished user interface that is ready to connect to the FastAPI backend in the next sprint.

---

# Existing Project Structure

The application already exists at

```
apps/executive-research
```

Technology stack:

- Next.js App Router
- TypeScript
- Tailwind CSS
- ESLint

Already installed

- lucide-react
- react-hook-form
- zod
- @hookform/resolvers
- clsx

---

# Scope

Implement only the frontend.

Do NOT implement:

- API calls
- FastAPI
- Runtime integration
- PDF generation
- Authentication
- History
- Database

---

# Required Folder Structure

Create (if not already present)

```
src/
│
├── app/
│
├── components/
│   ├── buttons/
│   ├── cards/
│   ├── common/
│   ├── forms/
│   ├── layout/
│   └── progress/
│
├── hooks/
├── lib/
├── services/
├── styles/
└── types/
```

---

# Required Components

Implement the following components.

## Header

Path

```
src/components/layout/Header.tsx
```

Responsibilities

- Display application title
- Display subtitle
- Center aligned
- Professional typography

Title

```
Executive Research
```

Subtitle

```
Generate executive-ready research reports using AI Agent Lab.
```

---

## Footer

Path

```
src/components/layout/Footer.tsx
```

Display

```
Powered by AI Agent Lab

Built by Sri Krishna Prasad
```

Keep minimal.

---

## QueryInput

Path

```
src/components/forms/QueryInput.tsx
```

Requirements

- Large multiline textarea
- Placeholder

```
Analyze the impact of AI Agents on Enterprise SaaS...
```

- Generate button

Use

- React Hook Form
- Zod validation

Validation

- Required
- Minimum 20 characters
- Maximum 5000 characters

Button

```
Generate Executive Report
```

Button must become disabled while processing.

For this sprint use mocked processing.

---

## ProgressTracker

Path

```
src/components/progress/ProgressTracker.tsx
```

Display four steps

```
Planning

Research

Summary

Report Generation
```

Each step supports

- pending
- running
- completed

Initially hidden.

Visible after Generate is clicked.

---

## ExecutiveSummaryCard

Path

```
src/components/cards/ExecutiveSummaryCard.tsx
```

Display

```
Executive Summary
```

Card body

Use mocked summary text.

Initially hidden.

Visible after processing.

---

## KeyInsightsCard

Path

```
src/components/cards/KeyInsightsCard.tsx
```

Display

```
Key Insights
```

Use mocked insights

Example

- Insight 1
- Insight 2
- Insight 3

Use Lucide Check icon.

Initially hidden.

---

## DownloadButton

Path

```
src/components/buttons/DownloadButton.tsx
```

Display

```
Download Executive Report (PDF)
```

Mock only.

Do not generate PDFs.

Initially hidden.

Visible after report generation.

---

# Main Page

Replace

```
src/app/page.tsx
```

Compose the page using only reusable components.

Order

```
Header

QueryInput

ProgressTracker

ExecutiveSummaryCard

KeyInsightsCard

DownloadButton

Footer
```

Maximum width

```
960px
```

Center aligned.

Responsive.

---

# Mock Behaviour

No backend.

Simulate workflow.

After clicking Generate

Wait approximately

```
2 seconds
```

Then

Show

Progress

↓

Executive Summary

↓

Key Insights

↓

Download Button

---

# Styling

Professional SaaS application.

Requirements

- Plenty of whitespace
- Rounded cards
- Soft shadows
- Tailwind only
- Responsive
- No external CSS frameworks
- No animation libraries

Color palette

Primary

```
#2563EB
```

Background

```
#F8FAFC
```

Cards

```
#FFFFFF
```

Text

```
#0F172A
```

Success

```
#16A34A
```

Border

```
#E2E8F0
```

---

# Code Quality

Follow

- SOLID where applicable
- Single Responsibility Principle
- Reusable components
- Strict TypeScript
- No unused imports
- No any types
- No duplicated code

---

# Deliverables

A working frontend with

- Header
- Query input
- Mock processing
- Executive Summary
- Key Insights
- Download button
- Footer

---

# Validation

Run

```bash
npm run lint
```

Fix all lint issues.

Run

```bash
npm run dev
```

Ensure the application loads successfully.

---

# Definition of Done

The application:

- Compiles successfully.
- Has no TypeScript errors.
- Has no ESLint errors.
- Is fully responsive.
- Uses reusable components.
- Displays mocked Executive Summary.
- Displays mocked Key Insights.
- Displays mocked Download button.
- Requires no backend.

---

# Stop Conditions

Do NOT

- Implement APIs
- Implement FastAPI
- Connect AI Agent Lab runtime
- Generate PDFs
- Add authentication
- Add report history
- Introduce unnecessary dependencies
- Change project structure outside the defined scope

Focus only on delivering a production-ready frontend foundation.