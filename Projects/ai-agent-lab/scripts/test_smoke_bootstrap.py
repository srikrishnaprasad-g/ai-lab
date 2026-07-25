"""Smoke test for RuntimeBootstrap."""
from runtime.runtime_bootstrap import RuntimeBootstrap
from registry.agent_registry import AgentRegistry

def test_bootstrap():
    orchestrator = RuntimeBootstrap.build()
    
    # Verify Orchestrator initialized
    assert orchestrator is not None
    
    # Verify Registry contains expected agents
    registry = orchestrator._registry
    assert registry.exists("research_agent")
    assert registry.exists("summary_agent")
    assert registry.exists("pdf_agent")
    
    print("RuntimeBootstrap smoke test PASSED.")

if __name__ == "__main__":
    test_bootstrap()
