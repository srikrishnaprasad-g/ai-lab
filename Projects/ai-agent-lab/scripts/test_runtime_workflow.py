"""Integration smoke test for the complete runtime workflow."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import sys
from runtime.bootstrap import RuntimeBootstrap


def run_smoke_test() -> None:
    """Executes the complete runtime workflow and validates the results."""
    print("Starting Runtime Workflow Smoke Test...")

    # Build runtime
    runtime = RuntimeBootstrap.build_runtime()

    # Execute workflow
    request = "Research AI Agents"
    runtime_result = runtime.execute(request)
    context = runtime_result.context

    # Validation
    errors = []

    # 1. Validate result
    if not runtime_result.result.success:
        errors.append("Runtime result success is False")

    # 2. Validate memory
    if "search_results" not in context.working_memory:
        errors.append("search_results missing from memory")
    if "research_summary" not in context.working_memory:
        errors.append("research_summary missing from memory")
    if "final_summary" not in context.working_memory:
        errors.append("final_summary missing from memory")

    # 3. Validate artifacts
    if len(context.artifacts) != 1:
        errors.append(f"Expected 1 artifact, found {len(context.artifacts)}")
    elif context.artifacts[0].name != "research_summary.pdf":
        errors.append(f"Unexpected artifact name: {context.artifacts[0].name}")

    # 4. Validate trace
    # Expected order: web search, research, summary, pdf, root
    expected_components = ["mock_web_search", "mock_research_agent", "mock_summary_agent", "mock_pdf_tool", "root"]
    actual_components = [event.component for event in context.execution_trace]
    
    if actual_components != expected_components:
        errors.append(f"Execution order mismatch. Expected {expected_components}, got {actual_components}")

    # Report
    if errors:
        print("\nSmoke Test FAILED:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("\nSmoke Test PASSED: Workflow executed correctly.")
        sys.exit(0)


if __name__ == "__main__":
    run_smoke_test()
