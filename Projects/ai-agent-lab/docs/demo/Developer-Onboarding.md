# Developer Onboarding

## Repository Layout
- `agents/`: Agent implementations.
- `runtime/`: Orchestration and execution logic.
- `llm/`: LLM provider abstractions.
- `tools/`: Tool abstractions and implementations.
- `prompts/`: Prompt builders and registry.
- `docs/`: Architecture and design documentation.
- `scripts/`: Diagnostic scripts.
- `tests/`: Unit and integration tests.

## Running Locally
1. Ensure Python 3.13+ is installed.
2. Install dependencies: `pip install -r requirements.txt` (or appropriate method).
3. Set up `.env` with required API keys (e.g., GEMINI_API_KEY).
4. Run diagnostics: `python scripts/verify_settings.py`

## Adding a New Agent
1. Inherit from `BaseAgent`.
2. Implement `_execute(context)`.
3. Register the agent in `AgentRegistry`.
4. Update `TaskPlanner` if the agent participates in the standard workflow.
