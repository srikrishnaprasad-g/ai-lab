# Sprint 3.7 – Executive Research UI Polish & Architecture Refinement

## Role

You are a Senior Frontend Engineer and UI Architect.

Your responsibility is NOT to add new business functionality.

Your responsibility is to refine the existing frontend into a production-quality SaaS interface while improving maintainability and preparing it for backend integration.

---

# Mandatory Preparation

Before making changes:

1. Read

```
docs/product/EXECUTIVE_RESEARCH_PRD.md
```

2. Read

```
docs/product/UI_SPECIFICATION.md
```

3. Review the existing implementation under

```
apps/executive-research/src
```

Understand the current component hierarchy before modifying anything.

---

# Objective

Refactor and polish the frontend without changing the user flow.

Do NOT implement backend functionality.

The application should look and feel like a professional SaaS product suitable for inclusion in a public portfolio.

---

# Scope

Only improve the frontend.

Do NOT modify:

- FastAPI
- APIs
- Runtime integration
- PDF generation
- Authentication

---

# Refactoring Tasks

## 1. Create Shared UI Components

Introduce reusable UI primitives.

Suggested structure

```
src/components/common/

Card.tsx

Button.tsx

Section.tsx

PageContainer.tsx
```

Existing components should use these primitives.

Avoid duplicated styling.

---

## 2. Create Shared Types

Create

```
src/types/research.ts
```

Example

```ts
export interface ResearchResult {
    executiveSummary: string;
    keyInsights: string[];
}
```

Also create any other reusable types if appropriate.

---

## 3. Create Mock Service

Create

```
src/services/mockResearchService.ts
```

Move all mocked report generation here.

The service should expose

```ts
generateMockResearchReport(query: string)
```

The page should no longer contain inline mocked data.

---

## 4. Create Custom Hook

Create

```
src/hooks/useExecutiveResearch.ts
```

Move all UI state management into this hook.

Examples

- processing state

- progress

- results

- mock service calls

The page component should become mostly composition.

---

## 5. Improve Progress Tracker

Replace simple colored circles with clearer status indicators.

Examples

Completed

✓

Running

Animated indicator

Pending

Outlined circle

Display connecting lines between steps.

---

## 6. Improve Cards

Executive Summary

- Better typography
- Better spacing
- Better readability

Key Insights

- Better list spacing
- Stronger visual hierarchy

---

## 7. Improve Layout

Increase whitespace.

Improve section spacing.

Improve card spacing.

Improve mobile responsiveness.

Maintain maximum width of

```
960px
```

---

## 8. Improve Button Styling

Buttons should have

- hover state

- focus state

- disabled state

- loading state

No animation libraries.

CSS only.

---

## 9. Improve Empty State

Before a report is generated

Display a helpful message encouraging users to enter a research question.

Do not leave the page feeling empty.

---

## 10. Improve Loading State

Display a professional loading experience.

Keep it subtle.

Avoid spinners if possible.

---

## 11. Accessibility

Verify

- keyboard navigation

- focus indicators

- semantic HTML

- ARIA labels where appropriate

---

## Code Quality

Follow

- SOLID principles
- Single Responsibility Principle
- Reusable components
- Strict TypeScript
- No duplicated logic
- No unused imports
- No unnecessary dependencies

---

## Validation

Run

```bash
npm run lint
```

Resolve all warnings.

Run

```bash
npm run dev
```

Verify responsive layout.

---

## Deliverables

A polished frontend ready for backend integration.

---

## Definition of Done

The application

- looks like a modern SaaS product

- uses reusable UI primitives

- uses shared types

- uses a custom hook

- uses a mock service

- contains no inline mocked data

- has responsive layouts

- passes lint

- is ready for FastAPI integration

---

## Implementation Report

At the end, provide

1. Files Created

2. Files Modified

3. Files Deleted

4. Dependencies Added

5. Commands Executed

6. Validation Performed

7. Assumptions Made

8. Remaining Work