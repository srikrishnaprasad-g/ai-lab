# Architecture Delta (Sprint 7)

## Architecture Before Sprint 7
- Simulated/Deterministic summarization logic in `SummaryAgent`.
- No LLM provider integration.
- Placeholder findings injected via defensive parsing.
- Minimal observability (no structured tracing of the LLM path).
- System prompts were often concatenated into the user prompt or hardcoded.

## Architecture After Sprint 7
- **LLM Integration:** `SummaryAgent` fully integrated with `LLMProvider` abstraction.
- **Provider Injection:** `LLMProvider` injected via `RuntimeBootstrap` and `AgentFactory`.
- **System Prompting:** Utilizes Gemini API's `systemInstruction` field for structured instructions.
- **Observability:** Pipeline instrumented with structured logging for every stage (CLI, Planner, Agent, Provider, API).
- **Resilience:** Implemented aggressive JSON extraction and strict contract validation, moving away from silent fallback placeholders.

## Major Improvements
- **Decoupled Prompt Logic:** Prompt building now consistently separates system/user prompts.
- **Production Observability:** Stage-by-stage tracing in `verbose` mode.
- **JSON Contract Enforcement:** Explicit parsing and validation logic replacing deterministic simulations.

## New Abstractions & Contracts
- `LLMRequest.system_prompt` field.
- JSON response schema contract (enforced by LLM instructions and local validation).

## Architectural Trade-offs
- Increased complexity in `SummaryAgent` due to robust JSON parsing requirements.
- Dependency injection dependency on `LLMProvider` for all agents requiring LLM interaction.

## Remaining Weaknesses & Future Recommendations
- **TD-017:** Extract robust JSON parser into a dedicated component.
- **Dynamic Planner:** Move from hardcoded task graph to dynamic planning (TD-004).
- **PDF Formatting:** Continue to improve `ReportLabGenerator` rendering capabilities.
