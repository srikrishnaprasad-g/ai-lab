"""Unit tests for the Agent Framework."""

from context.request_context import RequestContext
from agents.agent_factory import AgentFactory
from agents.agent_result import AgentResult
from agents.base_agent import BaseAgent
from observability.telemetry_service import TelemetryService
from registry.agent_registry import AgentRegistry
from agents.agent_capabilities import AgentCapabilities

# Mock TelemetryService
class MockTelemetryService(TelemetryService):
    def start_span(self, name, component, trace_id):
        return "span_id"
    def end_span(self, span):
        pass

# Mock BaseAgent for testing
class MockAgent(BaseAgent):
    def __init__(self, telemetry_service):
        capabilities = AgentCapabilities(supported_tools=["tool1"])
        super().__init__("mock_agent", "description", telemetry_service, capabilities)
        
    def _execute(self, context: RequestContext) -> AgentResult:
        if context.user_request == "fail":
            raise ValueError("Intentional error")
        return AgentResult(success=True, output="success")

def test_base_agent_lifecycle():
    print("Testing base agent lifecycle...")
    telemetry = MockTelemetryService()
    agent = MockAgent(telemetry)
    
    assert agent.name() == "mock_agent"
    assert "tool1" in agent.capabilities.supported_tools
    
    # Test execute wrapper
    context = RequestContext(request_id="1", correlation_id="c1", user_request="test")
    result = agent.execute(context)
    assert result.success is True
    assert result.output == "success"
    print("Base agent lifecycle PASSED.")

def test_agent_exception_handling():
    print("Testing exception handling...")
    telemetry = MockTelemetryService()
    agent = MockAgent(telemetry)
    
    context = RequestContext(request_id="1", correlation_id="c1", user_request="fail")
    
    try:
        agent.execute(context)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Intentional error"
    print("Exception handling PASSED.")

def test_agent_factory():
    print("Testing agent factory...")
    telemetry = MockTelemetryService()
    factory = AgentFactory(telemetry)
    agent = factory.create_research_agent()
    assert agent.name() == "research_agent"
    print("Agent factory PASSED.")

def test_agent_registry():
    print("Testing agent registry...")
    registry = AgentRegistry()
    telemetry = MockTelemetryService()
    agent = MockAgent(telemetry)
    
    registry.register(agent)
    assert registry.get(agent.name()) == agent
    print("Agent registry PASSED.")

if __name__ == "__main__":
    test_base_agent_lifecycle()
    test_agent_exception_handling()
    test_agent_factory()
    test_agent_registry()
    print("All tests PASSED.")
