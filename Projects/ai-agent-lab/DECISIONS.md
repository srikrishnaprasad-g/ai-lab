# Decision Log

| ADR     | Title                              | Status   |
| ------- | ---------------------------------- | -------- |
| ADR-001 | Stateless Tools                    | Accepted |
| ADR-002 | RequestContext Ownership           | Accepted |
| ADR-003 | Provider-Based Integration Pattern | Accepted |
| ADR-004 | Repository Health Policy           | Accepted |
| ADR-005 | Documentation Governance           | Accepted |
| ADR-006 | Definition of Done                 | Accepted |
| ADR-007 | Incremental Architecture Evolution | Accepted |
| ADR-008 | Architecture Freeze                | Accepted |
| ADR-009 | Runtime owns Orchestration         | Accepted |
| ADR-010 | Execution Pipeline                 | Accepted |
| ADR-011 | Planning vs Execution              | Accepted |
| ADR-012 | Stable Runtime Contracts           | Accepted |
| ADR-013 | Planner Abstraction                | Accepted |
| ADR-014 | Runtime Orchestrator               | Accepted |
| ADR-015 | Production Agent Framework         | Accepted |
| ADR-016 | TypedWorkflowContext Compatibility | Accepted |

-----

# ADR-001

Tools are stateless.
Execution state belongs to RequestContext.
---

# ADR-002

RequestContext owns runtime state.
Agents own decisions.
Tools own execution.
Providers own LLM communication.
----

## ADR-003: Provider-Based Integration Pattern

Status: Accepted

Decision:
External integrations shall use Provider abstractions (e.g., SearchProvider, LLMProvider).

RuntimeBootstrap is responsible for resolving configuration and injecting providers into Tools or Agents.

Rationale:
- Enables dependency injection
- Simplifies testing
- Allows provider swapping without changing business logic
- Keeps runtime components framework-agnostic

-----

ADR-004

Repository Health is mandatory before sprint closure.

Critical findings block sprint completion.

Recommended and Future findings must be tracked.

-----

ADR-005

PROJECT.md

defines WHAT we build.

ENGINEERING.md

defines HOW we build.

GEMINI.md

defines HOW AI contributes.

DECISIONS.md

defines WHY architectural decisions were made.

------

ADR-006

A task cannot be considered complete until:

- Validation passes.
- Documentation updated.
- Repository reviewed.
- Technical debt updated.

-----
ADR-007 - Incremental Architecture Evolution

Decision

The project adopts incremental architecture evolution.

Principles

Prefer extending existing abstractions.

Avoid speculative abstractions.

Avoid introducing new packages without immediate need.

Favor backwards compatibility.

Architecture changes should support current roadmap objectives.

------

ADR-008 – Architecture Freeze During Feature Sprints

Decision:

Infrastructure changes are prohibited during feature sprints unless required to support the planned functionality.

Allowed:

new agents
new prompts
new orchestration logic
new tools

Not allowed:

moving packages
renaming folders
registry redesign
dependency injection redesign
configuration redesign

------

ADR 009 - Runtime owns Orchestration

Decision

Workflow orchestration belongs exclusively to the Runtime.

Rationale

Keeps agents reusable.

Benefits

Separation of concerns

Simpler testing

Predictable workflows

----- 

ADR 010 - Execution Pipeline

Decision

Cross-cutting runtime behaviors
shall execute through the Execution Pipeline.

Examples

Retry

Telemetry

Timeout

Future

Caching

Authorization

Rate Limiting

-----

ADR 011 - Planning s Execution

Decision

Planning decides WHAT should happen.

Execution decides HOW it happens.

Agents perform the domain work.

No component may combine all three responsibilities.

-----

ADR 012 — Stable Runtime Contracts

Decision

Core runtime contracts must remain stable across implementation sprints.

Contracts include:

RequestContext
AgentId
AgentResult
ExecutionAction
ExecutionDecision
RuntimeResult

-----

## ADR-013 - Planner Abstraction

Status: Accepted

Decision:
The Planner component is responsible for deciding the next execution action based on the RequestContext.

Rationale:
Separates planning (WHAT) from execution (HOW) as defined in ADR-011.

## ADR-014 - Runtime Orchestrator

Status: Accepted

Decision:
The Runtime Orchestrator coordinates the execution flow by invoking the Planner to determine the next action, validating that action, and executing the final callback through the Execution Pipeline.

Rationale:
Separates orchestration from planning and execution as defined in ADR-011.

## ADR-015 - Production Agent Framework

Status: Accepted

Decision:
All production agents must inherit from `BaseAgent`, which provides a standardized lifecycle, telemetry hooks, logging, and error handling. Business logic must be implemented in the `_execute` method.

Rationale:
Ensures consistency, standardized telemetry, and robust error handling across all agents while decoupling business logic from reusable agent infrastructure.

## ADR-016 — TypedWorkflowContext Compatibility

Status: Accepted

Decision

- RequestContext remains the canonical runtime execution contract.
- TypedWorkflowContext extends RequestContext.
- RuntimeOrchestrator operates on TypedWorkflowContext.
- BaseAgent and all production agents continue to accept RequestContext.
- Existing public agent APIs remain unchanged.

Rationale

This preserves backward compatibility, complies with the architecture freeze, and resolves the runtime integration contract mismatch discovered during Sprint 6.5C.