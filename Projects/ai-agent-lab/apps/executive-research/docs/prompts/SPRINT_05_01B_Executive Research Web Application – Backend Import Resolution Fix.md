# Backend Import Resolution Fix

## Context

The frontend is working correctly.

The remaining blocker is that the FastAPI backend cannot import the AI Agent Lab runtime.

Current error:

```
ModuleNotFoundError: No module named 'runtime'
```

The runtime exists in the AI Agent Lab project.

This is an import resolution problem.

It is NOT a runtime problem.

---

## Objective

Fix the backend so that it can correctly import the existing AI Agent Lab runtime without requiring manual PYTHONPATH modifications.

The solution should be production-ready.

---

## Constraints

Do NOT:

- duplicate runtime
- move runtime
- copy runtime
- change runtime architecture

Instead:

Use proper Python packaging/import mechanisms.

---

## Investigate

Determine:

1. Why backend cannot resolve runtime.
2. Whether the project root should be added automatically.
3. Whether editable installation is required.
4. Whether __init__.py files are missing.
5. Whether imports should be absolute or package-based.
6. Whether uvicorn should be started differently.

Choose the cleanest production solution.

---

## Validation

After the fix, this command should work:

```

uvicorn app.main:app --reload

```

without requiring manual environment configuration.

---

## Deliverables

Provide:

1. Root cause
2. Files modified
3. Fix implemented
4. Validation
5. Recommended startup command

Do not modify unrelated code.