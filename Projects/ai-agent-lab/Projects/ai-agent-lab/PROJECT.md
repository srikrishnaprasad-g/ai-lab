# AI Agent Lab

## Vision

Build a production-quality modular AI Agent that demonstrates:

- Multi-agent orchestration
- Dynamic tool selection
- Multi-model routing
- Observability
- OpenTelemetry tracing
- PUVINoise telemetry integration
- Production engineering practices

The project is intended as a learning platform for modern AI Agent architectures while also serving as a telemetry demonstration for PUVINoise.

---

# Design Principles

1. Keep components small and modular.
2. Every LLM interaction must be observable.
3. Every tool execution must generate telemetry.
4. Keep business logic independent from CLI/UI.
5. Prefer composition over inheritance.
6. Write clean, readable Python.
7. Use async where appropriate.
8. Avoid framework lock-in.

---

# High-Level Architecture

User

↓

Orchestrator Agent

↓

Planner

↓

Task Router

↓

Specialized Agents

↓

Tools

↓

LLM Providers

↓

Response

Every step must emit telemetry.

---

# Planned Agents

## Phase 1

- Main Agent

## Phase 2

- Planner Agent
- Research Agent
- Writer Agent

## Phase 3

- Coding Agent
- Critic Agent
- Memory Agent

---

# Planned Tools

- Web Search
- Calculator
- File Reader
- Memory
- SQL
- Git

Each tool must be independently testable.

---

# LLM Providers

Initially:

- Gemini 2.5

Future:

- OpenAI
- Claude
- DeepSeek
- Qwen

The architecture must allow easy addition of new providers.

---

# Telemetry Goals

Capture:

- Trace ID
- Parent Span
- Agent Name
- Tool Name
- Model
- Prompt Length
- Response Length
- Latency
- Token Usage (when available)
- Errors
- Retry Count

Telemetry should follow OpenTelemetry standards wherever possible.

---

# Folder Structure

agents/
llm/
telemetry/
tools/
prompts/
tests/

---

# Coding Standards

- Python 3.12+
- Type hints everywhere
- Docstrings for public classes
- Logging instead of print()
- Small functions
- Clear separation of concerns

---

# Git Workflow

After every working milestone:

- Run tests
- Commit changes
- Keep commits small
- Use descriptive commit messages

---

# Current Phase

Phase 1

Goal:

Build a single modular AI Agent using Gemini with structured logging and telemetry.

No multi-agent orchestration yet.

Focus on architecture.

---

# Future Roadmap

Phase 2
- Planner Agent

Phase 3
- Tool Selection

Phase 4
- Parallel Execution

Phase 5
- Multi-model Routing

Phase 6
- Reflection Agent

Phase 7
- Evaluation Agent

Phase 8
- Human Approval Workflow

Phase 9
- Production Observability Dashboard

---

# Success Criteria

The project should eventually demonstrate:

- Agent orchestration
- Tool orchestration
- Tracing
- Retry handling
- Error recovery
- Parallel execution
- Rich telemetry inside PUVINoise