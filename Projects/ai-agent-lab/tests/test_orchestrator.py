"""Unit tests for RuntimeOrchestrator."""
from unittest.mock import MagicMock
from runtime.orchestrator.orchestrator import RuntimeOrchestrator
from runtime.orchestrator.task_graph import TaskGraph, TaskNode
from runtime.models.workflow import WorkflowDefinition
from runtime.models.plan import ExecutionPlan
from runtime.models.context import TypedWorkflowContext
from registry.agent_registry import AgentRegistry
from agents.base_agent import BaseAgent
from runtime.pipeline.execution_pipeline import ExecutionPipeline

def test_orchestrator_execution():
    registry = MagicMock(spec=AgentRegistry)
    pipeline = MagicMock(spec=ExecutionPipeline)
    planner = MagicMock()
    orchestrator = RuntimeOrchestrator(planner, pipeline, registry)
    
    # Mock Workflow
    graph = TaskGraph()
    graph.add_task(TaskNode(agent_id="agent1"))
    workflow = WorkflowDefinition(name="wf", plan=ExecutionPlan(), task_graph=graph)
    
    # Mock Context
    context = TypedWorkflowContext(request_id="1", correlation_id="c1", user_request="test")
    context.set("final_result", "done")
    
    # Mock Agent
    agent = MagicMock(spec=BaseAgent)
    agent.name.return_value = "agent1"
    registry.get.return_value = agent
    
    result = orchestrator.execute(workflow, context)
    
    assert result == "done"
    pipeline.execute.assert_called_once()
    print("Orchestrator test passed.")

if __name__ == "__main__":
    test_orchestrator_execution()
