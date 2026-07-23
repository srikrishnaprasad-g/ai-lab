# Known Limitations

## Current Constraints
- The `TaskPlanner` is currently static (hardcoded graph).
- PDF generation depends on `ReportLabGenerator`.
- Dependency injection is primarily handled in `RuntimeBootstrap`.
- Some observability features (e.g., custom span attributes) are still evolving.

## Deferred Work
- Dynamic Plan generation (TD-004).
- Parallel execution support (Roadmap Phase 4).
- Human-in-the-loop workflows (Roadmap Phase 8).
- Full PUVINoise integration dashboard (Roadmap Phase 9).
