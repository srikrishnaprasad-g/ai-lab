"""Unit tests for TaskGraph."""
from runtime.orchestrator.task_graph import TaskGraph, TaskNode

def test_task_graph_execution_order():
    graph = TaskGraph()
    graph.add_task(TaskNode(agent_id="agent1"))
    graph.add_task(TaskNode(agent_id="agent2", dependencies=["agent1"]))
    
    # First step
    executable = graph.get_executable_tasks([])
    assert executable == ["agent1"]
    
    # Second step
    executable = graph.get_executable_tasks(["agent1"])
    assert executable == ["agent2"]
    
    # Completed
    executable = graph.get_executable_tasks(["agent1", "agent2"])
    assert executable == []

if __name__ == "__main__":
    test_task_graph_execution_order()
    print("All Phase 2 tests PASSED.")
