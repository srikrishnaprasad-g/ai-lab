# Release Notes - v0.6.0-rc1

## Highlights
This release candidate marks the successful foundation of the Multi-Agent Runtime, featuring dynamic orchestration, modular agents, and robust provider abstractions.

## Major Features
- Production-ready Multi-Agent Orchestrator.
- Integrated Research, Summary, and PDF agents.
- Search and LLM provider abstraction layer.

## Architecture
- Composition root pattern (`RuntimeBootstrap`).
- Execution Pipeline for cross-cutting concerns (telemetry, retry).
- Stateless tool execution.

## Known Limitations
- Static Task Graph planning (to be dynamic in future).
- PDF generation tied to ReportLab.

## Technical Debt
- See `docs/TECHNICAL_DEBT.md` for full list of open items.

## Breaking Changes
- None (First official release candidate).

## Repository State
- Stable, validated, and documentation-complete.
