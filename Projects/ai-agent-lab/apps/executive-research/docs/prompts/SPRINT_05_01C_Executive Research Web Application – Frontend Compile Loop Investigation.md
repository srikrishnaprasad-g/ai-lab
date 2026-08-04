# Frontend Compile Loop Investigation

## Context

The FastAPI backend starts successfully.

The backend is NOT the current blocker.

The frontend loads in the browser, but the page repeatedly recompiles and becomes unusable.

Observed behavior:

- UI renders.
- "Compiling..." repeatedly appears.
- User cannot interact with the page.
- Terminal repeatedly reports:

```
FATAL: An unexpected Turbopack error occurred.
```

No requests are sent to the backend because the frontend never reaches an interactive state.

## Your Task

Determine the root cause of the frontend compile loop.

Investigate:

1. Is this caused by Turbopack?
2. Is there an infinite React render loop?
3. Is there a `useEffect` dependency loop?
4. Is there an automatic state update causing recompilation?
5. Is Fast Refresh continuously invalidating the page?
6. Does the project work correctly when using Webpack instead of Turbopack?

## Validation

After the fix:

- The page loads.
- No continuous recompilation occurs.
- The text box is editable.
- The Generate Report button is clickable.
- The frontend remains stable for several minutes.
- Only then verify communication with the backend.

Do not modify backend code.
Do not modify runtime code.
Focus only on the frontend.