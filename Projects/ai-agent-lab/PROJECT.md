# AI Agent Lab

## Vision

Build a production-quality modular Multi-Agent Runtime capable of orchestration, tool execution, provider abstraction, and observability that demonstrates:

- Multi-agent orchestration
- Dynamic tool selection
- Multi-model routing
- Observability
- OpenTelemetry tracing
- PUVINoise telemetry integration
- Production engineering practices

The project is intended as a learning platform for modern AI Agent architectures while also serving as a telemetry demonstration for PUVINoise.

---

## MVP Scenario

                 User

                   │

                   ▼

         Orchestrator Agent

                   │

         "How do I solve this?"

                   │

         Creates Execution Plan

                   │

      ┌────────────┴────────────┐
      ▼                         ▼

Research Agent          Writer Agent

      │                         │

Web Search Tool         Summarization

      │                         │

      ▼                         ▼

      Search Results       Draft Summary

              │

              ▼

         PDF Agent

              │

      PDF Generation Tool

              │

              ▼

          PDF File

              │

              ▼

         Return to User

The first end-to-end workflow for this project is:

Research Topic
    ↓
Web Search
    ↓
Research Agent
    ↓
Summary Generation
    ↓
PDF Report Generation
    ↓
Return PDF to User

All future architectural decisions should support this workflow.

What happens internally?

                 User

                   │

                   ▼

         Orchestrator Agent

                   │

         "How do I solve this?"

                   │

         Creates Execution Plan

                   │

      ┌────────────┴────────────┐
      ▼                         ▼

Research Agent          Writer Agent

      │                         │

Web Search Tool         Summarization

      │                         │

      ▼                         ▼

      Search Results       Draft Summary

              │

              ▼

         PDF Agent

              │

      PDF Generation Tool

              │

              ▼

          PDF File

              │

              ▼

         Return to User

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

OrchestratorAgent

↓

Planner

↓

Task Graph

↓

Specialized Agents

↓

Tool Registry

↓

Tools

↓

LLM Providers

↓

Response


The runtime should expose sufficient execution information to allow observability tooling such as PUVINoise to instrument execution

---

# Current Development Environment

Workspace:
C:\AI-LAb\projects\ai-agent-lab

Development Tool:
Claude Code

LLM Router:
Claude Code Router (CCR)

Primary Model:
Gemini 2.5 Flash

Fallback Model:
Groq (Qwen 3.6 27B)

Version Control:
Git

Language:
Python

Observability:
PUVINoise

---

# Architecture Principles

- LLM providers must be replaceable.
- Agents must not depend on provider implementations.
- Tool execution must be observable.
- Telemetry should use OpenTelemetry standards.
- Business logic must remain independent of the CLI.
- Components should have a single responsibility.

---

# Planned Agents

## Phase 1

- Orchestrator Agent

## Phase 2

- Planner Agent
- Research Agent

## Phase 3

- Coding Agent
- Analysis Agent
- Critic Agent
- Memory Agent

---

# Planned Tools

- Search
- Calculator
- File Reader
- Memory
- SQL
- Git
- Python
- HTTP
- Browser
- PDF Reader

Each tool must be independently testable.

---

# LLM Providers

Initially:

- Gemini 2.5
- Groq

Future:

- OpenAI
- Claude
- DeepSeek
- Qwen
- Ollama

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

ai-agent-lab/

agents/
llm/
telemetry/
tools/
prompts/
config/
docs/
tests/

---

# Living Architecture

This project is expected to evolve over time.

Major architectural decisions should be documented.

PROJECT.md describes the system.

ENGINEERING.md describes how we build it.

Future Architecture Decision Records (ADRs) will explain why important design decisions were made.

---

# Non Goals

This project is not intended to:

- Build a chatbot.
- Optimize benchmark scores.
- Depend on a single LLM provider.
- Become tied to one AI framework.

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

# Current Sprint

Sprint 1: Officially Complete

We've achieved much more than just writing code:

✅ Established a disciplined engineering workflow.
✅ Built a provider abstraction layer.
✅ Implemented Gemini and Groq providers (structure).
✅ Implemented a working provider factory.
✅ Validated compile, import, and runtime behavior.
✅ Verified direct Groq connectivity independently of CCR.
✅ Refined the project architecture and engineering documentation.

Sprint 2 – Multi-Agent Runtime Foundation
Sprint Goal

Build the foundational runtime for a production-quality multi-agent AI system. The runtime should be capable of receiving a user request, orchestrating specialized agents, selecting appropriate tools, interacting with LLM providers, and producing a unified response. This sprint focuses on the architecture and execution framework rather than implementing specific business capabilities.

No business-specific logic should be implemented in this sprint. The objective is to establish a clean, extensible runtime that future agents and tools can plug into.

Sprint 2 Roadmap
Task 2.1 – Agent Framework

Objective

Build the foundation for every future agent.

Deliverables
Create agents/ package
Create abstract Agent interface
Define common lifecycle methods
Add comprehensive documentation and type hints
Validation
Compile successfully
Smoke test agent instantiation
Git commit
Task 2.2 – Tool Framework

Objective

Create a common abstraction for every executable capability.

Deliverables
Create tools/ package
Create abstract Tool interface
Standardize tool execution contract
Tool metadata structure
Validation
Compile
Smoke test
Git commit
Task 2.3 – Request Context

Objective

Create a shared execution context that travels throughout the runtime.

Responsibilities

Store:

Request ID
User request
Intermediate results
Shared execution state
Metadata

This object will be passed between every agent.

Validation
Compile
Runtime validation
Git commit
Task 2.4 – Tool Registry

Objective

Create a registry responsible for discovering and providing available tools.

Responsibilities
Register tools
Discover tools
Retrieve tool instances
Future plugin support
Validation
Register dummy tools
Retrieve tools
Smoke test
Git commit
Task 2.5 – Orchestrator Agent

Objective

Build the runtime entry point.

Responsibilities
Accept user requests
Initialize RequestContext
Delegate work to specialized agents
Aggregate responses
Return final result

Important

The Orchestrator should not decide which tools to execute.

It only coordinates execution.

Validation
Simulated execution
Smoke test
Git commit
Task 2.6 – Research Agent

Objective

Build the first specialized agent.

Responsibilities
Understand research objectives
Decide when web search is required
Invoke Search Tool
Produce structured research output
Validation
Mock tool execution
Runtime validation
Git commit
Task 2.7 – Writer Agent

Objective

Transform research into a coherent report.

Responsibilities
Consume research output
Generate structured summary
Produce markdown-ready content
Validation
Mock inputs
Smoke test
Git commit
Task 2.8 – PDF Agent

Objective

Generate the final deliverable.

Responsibilities
Convert report into PDF
Return generated file path
Handle formatting
Validation
Generate sample PDF
Verify output
Git commit
Task 2.9 – End-to-End Runtime

Objective

Connect every component built during Sprint 2.

Expected Flow
User Request
      │
      ▼
Orchestrator Agent
      │
      ▼
Research Agent
      │
      ▼
Search Tool (Mock)
      │
      ▼
Writer Agent
      │
      ▼
PDF Agent
      │
      ▼
PDF Output

The Search Tool will initially be mocked. Real web search and LLM integrations will be introduced in Sprint 3.

Validation
Execute complete workflow
Smoke test
Git commit
Sprint 2 Deliverables

By the end of Sprint 2, the project will include:

Agent Framework
Tool Framework
Request Context
Tool Registry
Orchestrator Agent
Research Agent
Writer Agent
PDF Agent
End-to-End Runtime Skeleton

The runtime will execute a complete multi-agent workflow using mock implementations, providing a stable foundation for integrating real tools and LLM providers in subsequent sprints.

Sprint 2 Status

✅ Completed

Implemented:

• Runtime bootstrap
• Runtime orchestration
• Agent framework
• Tool framework
• Registry framework
• RequestContext
• RuntimeResult
• Mock research workflow
• End-to-end smoke testing

Ready for Sprint 3:
Replace mock implementations with production implementations.
- Real Web Search
- Real LLM Integration
- Real PDF Generation
- PUVINoise SDK Integration

Looking Ahead – Sprint 3 (Preview)

Sprint 3 will replace the mock components with real implementations:

Gemini Provider integration
Groq Provider integration
Web Search Tool
Prompt templates
Agent reasoning
Tool selection logic
Report quality improvements

## Sprint 3 Progress

Completed:
- Search Provider abstraction
- LLM Provider abstraction
- Prompt Builder framework
- Runtime Observability framework
- Runtime-managed telemetry

### Sprint 3 – Task 3.7 Completed

Implemented the production-ready Search Provider infrastructure.

Highlights:
- Generic HttpClient abstraction
- SearchProviderConfig
- Persistent HTTP connections (httpx.Client)
- Provider registry
- Generic HTTP exception hierarchy
- Configuration-driven provider initialization
- Production-ready dependency injection

### ✅ Task 3.8 – Production Gemini Provider

**Status:** Completed

#### Deliverables
- Implemented production-ready Gemini provider.
- Added configurable `LLMProviderConfig` supporting:
  - API Key
  - Model
  - API Version
  - Base URL
  - Timeout
- Integrated Gemini API using the shared HttpClient.
- Implemented GeminiResponseMapper for standardized response mapping.
- Removed hardcoded model selection.
- Provider now uses centralized configuration from `Settings`.
- Added validation for missing provider configuration.
- Unified LLM configuration using `DEFAULT_LLM_*` settings.
- Fixed environment loading using `.env`.
- Successfully validated end-to-end communication with the Gemini Developer API.

#### Validation
- Configuration loading verified.
- Factory wiring verified.
- Provider configuration verified.
- Successful API invocation.
- Response mapping verified.
- Token usage metadata verified.

**Status:** ✅ Passed

Current Runtime

User Request
      ↓
Search
      ↓
Research
      ↓
Prompt Builder
      ↓
LLM
      ↓
PDF Artifact
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