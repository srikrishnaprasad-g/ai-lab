from runtime.models.workflow import WorkflowDefinition
from runtime.models.plan import ExecutionPlan
from runtime.orchestrator.task_graph import TaskGraph, TaskNode

class ResearchWorkflowBuilder:
    @staticmethod
    def build() -> WorkflowDefinition:
        graph = TaskGraph()
        graph.add_task(TaskNode(agent_id="research_agent"))
        graph.add_task(TaskNode(agent_id="summary_agent", dependencies=["research_agent"]))
        graph.add_task(TaskNode(agent_id="pdf_agent", dependencies=["summary_agent"]))
        
        return WorkflowDefinition(
            name="research_workflow",
            plan=ExecutionPlan(),
            task_graph=graph
        )
