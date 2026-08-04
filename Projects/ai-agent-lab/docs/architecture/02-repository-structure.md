# Repository Structure

```
AI-Lab/

│
├── apps/
│   └── executive-research/
│       ├── frontend/
│       └── backend/
│
├── runtime/
│
├── agents/
│
├── providers/
│
├── shared/
│
├── docs/
│
└── tests/
```

## Responsibilities

### apps/

Contains user-facing applications.

Each application owns:

- UI
- Backend
- API
- Product Logic

Applications should not directly call LLM providers.

---

### runtime/

Contains reusable orchestration.

Examples

- workflow execution

- task scheduling

- memory

- context management

- prompt chaining

---

### agents/

Contains reusable AI agents.

Examples

- Research Agent

- Planner Agent

- Writer Agent

- Reviewer Agent

---

### providers/

Provider implementations.

Examples

- Gemini

- OpenAI

- Groq

- Ollama

Providers expose a common interface.

---

### shared/

Reusable utilities.

Examples

- Logging

- Config

- HTTP

- Types

- Exceptions