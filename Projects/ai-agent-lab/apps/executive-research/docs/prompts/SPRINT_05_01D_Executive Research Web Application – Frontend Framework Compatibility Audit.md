# Frontend Framework Compatibility Audit

## Context

The backend is fully operational.

The remaining blocker is the frontend.

Current runtime error:

```
Invariant: expected layout router to be mounted
```

The application now runs with Webpack instead of Turbopack.

The previous Turbopack issue exposed a deeper frontend framework issue.

---

# Objective

Determine the root cause of the App Router runtime error.

Do not guess.

Investigate the actual project structure.

---

# Investigate

Review:

- src/app/
- layout.tsx
- page.tsx
- providers
- hooks
- router usage
- navigation usage
- client/server component boundaries

Determine whether:

1. The App Router structure is valid.
2. Any component is using router APIs outside the App Router.
3. A Client Component is incorrectly nested.
4. A Server Component imports Client-only APIs.
5. React and Next.js versions are fully compatible.
6. The project is relying on APIs that changed in Next.js 16.

---

# Also investigate

The build reports mixed path casing:

```
Projects

vs

projects
```

Identify every location where inconsistent path casing is introduced.

Recommend the correct canonical casing.

---

# Constraints

Do NOT redesign the UI.

Do NOT redesign the backend.

Do NOT redesign AI Agent Lab.

Focus only on frontend framework compatibility.

---

# Deliverables

Provide:

1. Root cause.
2. Framework compatibility findings.
3. Required code changes.
4. Whether downgrading Next.js is recommended.
5. Validation after the fix.