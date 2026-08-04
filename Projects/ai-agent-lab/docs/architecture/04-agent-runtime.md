# AI Agent Runtime

## Responsibilities

The runtime is responsible for orchestration only.

It does not know anything about:

- FastAPI
- Next.js
- Products

It only executes workflows.

---

Example

Planner

↓

Research Agent

↓

Reviewer

↓

Writer

↓

Formatter

Each agent is independently testable.

The runtime coordinates them.

---

Future Features

- Memory

- Human approval

- Tool calling

- Multi-provider routing

- Parallel execution

- Retry policies

- Cost optimization

- Caching