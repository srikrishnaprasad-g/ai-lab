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