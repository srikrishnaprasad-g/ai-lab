# Executive Research — UI Redesign

11 files, all under `frontend/src/`, drop-in replacements for your
`ai-lab/Projects/ai-agent-lab/apps/executive-research/frontend/src/` tree.

## How to apply
Copy each file over its counterpart in your repo, preserving the same path, e.g.:

    cp frontend/src/app/layout.tsx  <your-repo>/.../executive-research/frontend/src/app/layout.tsx

No new dependencies were added — everything uses packages already in your
`package.json` (react-hook-form, zod, lucide-react, clsx, Tailwind v4).
`next/font/google` will fetch Fraunces, Inter, and IBM Plex Mono at build
time, same mechanism as your original Geist fonts, so this works out of the
box on Vercel.

## What changed and why

Old UI: default Tailwind slate/blue palette, Geist fonts, centered card —
reads as an unstyled MVP scaffold.

New direction: **a private research desk / briefing dossier.** The product's
actual job — turn a question into an executive report — became the design
brief itself, rather than defaulting to a generic SaaS-dashboard look.

- **Palette** — ink navy (`#12161f`) + warm paper (`#faf8f3`) + a muted
  brass accent (`#a9793d`). Not the default blue, not a generic
  terracotta/cream template.
- **Type** — Fraunces (editorial serif) for headlines and the pull-quote
  summary, Inter for body copy, IBM Plex Mono for structural labels
  (eyebrows, step numbers, timestamps, ref codes) — replacing Geist
  everywhere.
- **Signature element** — the progress tracker is now a vertical "briefing
  spine": a hairline that fills with brass as the agent runtime moves
  through Planning → Research → Summary → Report Generation. This is your
  actual pipeline sequence, not decorative step circles.
- **Results as a dossier** — the executive summary renders as an italic
  serif pull-quote with a dateline; key findings are numbered like an
  analyst's list of findings rather than generic bullet cards; the download
  action reads like a document stamp ("Report ready — REF ...") instead of
  a bare button.
- Empty and error states were designed rather than left as browser
  defaults — a quiet "nothing commissioned yet" prompt, and an error state
  that reads as "the desk couldn't complete this brief" rather than a raw
  error string.

## Files touched
- `app/layout.tsx` — font loading (Fraunces / Inter / IBM Plex Mono), metadata
- `app/globals.css` — full design-token system (color, hairlines, motion)
- `app/page.tsx` — page assembly, empty state, error state
- `components/layout/Header.tsx` — ink masthead
- `components/layout/Footer.tsx` — document-style footer
- `components/forms/QueryInput.tsx` — briefing-request form, live char counter
- `components/progress/ProgressTracker.tsx` — the briefing-spine tracker
- `components/common/Card.tsx` — base card styling
- `components/cards/ExecutiveSummaryCard.tsx` — dossier-style summary
- `components/cards/KeyInsightsCard.tsx` — numbered findings list
- `components/buttons/DownloadButton.tsx` — document-action download card

## Verified
- `tsc --noEmit` — clean
- `next build` — clean production build
- Interaction-tested end to end (query → progress → results) against the
  mock service with a headless browser — all four states screenshotted and
  reviewed: empty, filled input, in-progress (spine filling), completed
  results with summary/findings/download.

No backend or API contract changes — `researchApi.ts`, hooks, and types are
untouched.
