"""End-to-End validation for the complete runtime execution flow."""

from context.request_context import RequestContext
from runtime.runtime_bootstrap import RuntimeBootstrap
from registry.agent_registry import AgentRegistry

def run_e2e_tests() -> None:
    # 1. Bootstrapping
    orchestrator = RuntimeBootstrap.build()
    
    # 2. Setup
    context = RequestContext(request_id="1", correlation_id="c1", user_request="Explain Quantum Physics")
    
    # 3. Execution (Callback executes the research agent)
    def callback(ctx: RequestContext) -> str:
        # Retrieve agent and execute
        agent = orchestrator._agent_registry.get("research_agent")
        result = agent.execute(ctx)
        return result.output
        
    # 4. Action
    result = orchestrator.execute(context, callback)
    
    # 5. Validation
    print(f"Result: {result}")
    assert "Mock response" in result
    assert "Quantum Physics" in result
    print("End-to-End runtime flow PASSED.")

if __name__ == "__main__":
    run_e2e_tests()
