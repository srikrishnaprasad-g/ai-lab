"""Unit tests for runtime models."""
from runtime.models import TypedWorkflowContext, ExecutionPolicy, ExecutionPlan, WorkflowDefinition
from runtime.orchestrator.task_graph import TaskGraph

def test_typed_workflow_context():
    ctx = TypedWorkflowContext(request_id="1", correlation_id="c1", user_request="test")
    ctx.set("key", 123)
    assert ctx.get("key", int) == 123
    assert ctx.has("key")
    
    try:
        ctx.get("key", str)
        assert False, "Should raise TypeError"
    except TypeError:
        pass

def test_execution_policy_defaults():
    policy = ExecutionPolicy()
    assert policy.max_retries == 3
    assert policy.timeout_seconds == 30

def test_workflow_definition():
    plan = ExecutionPlan()
    graph = TaskGraph()
    wf = WorkflowDefinition(name="test_wf", plan=plan, task_graph=graph)
    assert wf.name == "test_wf"
    assert wf.plan == plan
    assert wf.task_graph == graph

if __name__ == "__main__":
    test_typed_workflow_context()
    test_execution_policy_defaults()
    test_workflow_definition()
    print("All Phase 1 tests PASSED.")
