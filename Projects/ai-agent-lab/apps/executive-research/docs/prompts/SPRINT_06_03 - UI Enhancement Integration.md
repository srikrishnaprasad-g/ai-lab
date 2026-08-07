Sprint 6.3 – UI Enhancement Integration (Workspace Verification First)

Context

The Executive Research application is already fully functional and deployed.

Production Frontend:
https://srikrishnaprasad-executive-summary.vercel.app

Production Backend:
https://executive-research-api.onrender.com

The complete workflow is already working:

✓ User submits a research query
✓ Tavily performs the research
✓ Gemini generates the executive summary
✓ Executive Summary and Key Insights are displayed
✓ PDF report is generated
✓ Download Report works
✓ Application is deployed successfully on Vercel + Render

This sprint is strictly a UI enhancement sprint.

Do NOT modify:

- backend
- FastAPI
- runtime
- agents
- workflow orchestration
- deployment configuration
- environment variables
- API contracts

The existing functionality must remain completely intact.

--------------------------------------------------
Phase 1 – Verify Frontend Workspace

Work ONLY inside:

Projects/ai-agent-lab/apps/executive-research/frontend

First verify the workspace is healthy.

Check that the following exist:

- package.json
- tsconfig.json
- next-env.d.ts
- node_modules

Run:

npm install

Verify these packages resolve correctly:

- react
- react-dom
- next
- typescript
- react-hook-form
- @hookform/resolvers
- zod
- lucide-react

If any dependency is missing, install ONLY the missing dependency.

Do not upgrade package versions unnecessarily.

--------------------------------------------------
Phase 2 – Integrate the New UI

The redesigned UI has already been extracted.

Use the source files from:

C:\AI-Lab\Projects\ai-agent-lab\executive-research-ui-redesign\Part 2\src

Copy all files and folders inside this src directory into:

C:\AI-Lab\Projects\ai-agent-lab\apps\executive-research\frontend\src

Overwrite existing files where necessary.

Merge the UI carefully.

Do NOT overwrite working API integration unless absolutely required.

--------------------------------------------------
Phase 3 – Protect Existing Functionality

This is the most important step.

Before making any changes, review these existing files:

- src/config/api.ts
- src/services/api/researchApi.ts
- src/components/buttons/DownloadButton.tsx

These production fixes MUST be preserved.

The frontend MUST continue calling:

Research API

${API_BASE_URL}/api/v1/research

Download API

${API_BASE_URL}/api/v1/download/${reportId}

Do not replace these with localhost.

Do not introduce hardcoded URLs.

Do not regress any existing functionality.

--------------------------------------------------
Phase 4 – Build Validation

Run:

npm run build

Resolve any compilation or TypeScript issues.

Then run:

npm run dev

--------------------------------------------------
Phase 5 – Functional Validation

Verify ALL of the following:

✓ Research request works

✓ Executive Summary displays

✓ Key Insights display

✓ Download Report downloads successfully

✓ Theme toggle works

✓ Theme preference persists after refresh

✓ "New Brief" clears the UI correctly

✓ Footer GitHub and LinkedIn links work

✓ Mobile responsiveness is preserved

✓ No console errors

✓ No broken imports

--------------------------------------------------
Phase 6 – Regression Checklist

Confirm that none of these production features regressed:

✓ NEXT_PUBLIC_API_BASE_URL usage

✓ API_BASE_URL configuration

✓ /api/v1/research endpoint

✓ /api/v1/download endpoint

✓ Report generation

✓ PDF download

✓ Executive Summary rendering

✓ Key Insights rendering

--------------------------------------------------
Deliverables

Provide:

1. Root cause of any issues found.
2. Dependencies installed (if any).
3. Files modified.
4. Build results.
5. Functional validation checklist.
6. Git diff.

Do NOT commit.

Do NOT push.

Stop after successful local validation.