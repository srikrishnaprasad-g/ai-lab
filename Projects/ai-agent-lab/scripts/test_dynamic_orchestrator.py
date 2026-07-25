"""E2E Integration test for the dynamic orchestrator using mock agents."""
import os
from unittest.mock import MagicMock
from runtime.orchestrator.orchestrator import RuntimeOrchestrator
from runtime.orchestrator.task_graph import TaskGraph, TaskNode
from runtime.models.workflow import WorkflowDefinition
from runtime.models.plan import ExecutionPlan
from runtime.models.context import TypedWorkflowContext
from registry.agent_registry import AgentRegistry
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from agents.research_agent import ResearchAgent
from agents.summary.summary_agent import SummaryAgent
from agents.pdf.pdf_agent import PDFAgent
from agents.pdf.mock_generator import MockPDFGenerator
from agents.summary.models.core import SummaryResult
from observability.telemetry_service import TelemetryService
from search.search_service import SearchService
from prompts.prompt_registry import PromptRegistry
from prompts.summary_prompt_builder import SummaryPromptBuilder

def run_e2e_integration():
    print("Initializing Mocked Orchestrator...")
    
    # Setup Mocks
    telemetry = MagicMock(spec=TelemetryService)
    search_service = MagicMock(spec=SearchService)
    # Return mock results for research
    search_service.perform_search.return_value = MagicMock(results=[], provider="mock")
    
    # Setup Agents
    registry = AgentRegistry()
    prompt_builder = SummaryPromptBuilder(PromptRegistry())
    
    research_agent = ResearchAgent(telemetry, search_service)
    llm_provider = MagicMock()
    summary_agent = SummaryAgent(telemetry, prompt_builder, llm_provider)
    pdf_generator = MockPDFGenerator()
    pdf_agent = PDFAgent(telemetry, pdf_generator)
    
    registry.register(research_agent)
    registry.register(summary_agent)
    registry.register(pdf_agent)
    
    # Setup Orchestrator
    pipeline = ExecutionPipeline([])
    planner = MagicMock() # Will mock the plan output
    orchestrator = RuntimeOrchestrator(planner, pipeline, registry)
    
    # Initialize TypedWorkflowContext
    context = TypedWorkflowContext(
        request_id="e2e_1",
        correlation_id="corr_1",
        user_request="Research Artificial Intelligence"
    )
    
    # Mock SummaryResult for PDF agent
    context.set("summary_result", SummaryResult(executive_summary="Test", key_findings=[], knowledge_gaps=[], citations=[], confidence=MagicMock()))
    
    # Build Graph
    graph = TaskGraph()
    graph.add_task(TaskNode(agent_id="research_agent"))
    graph.add_task(TaskNode(agent_id="summary_agent", dependencies=["research_agent"]))
    graph.add_task(TaskNode(agent_id="pdf_agent", dependencies=["summary_agent"]))
    workflow = WorkflowDefinition(name="research_to_pdf_workflow", plan=ExecutionPlan(), task_graph=graph)
    
    print("Executing dynamic orchestrator...")
    # Override orchestrator's execute to handle the workflow
    result = orchestrator.execute(workflow, context)
    
    # Validate final result (PDFResult)
    assert result is not None
    assert result.file_path.exists()
    
    # Clean up generated PDF
    if result.file_path.exists():
        os.remove(result.file_path)
        
    print("Dynamic Orchestration E2E Integration PASSED.")

if __name__ == "__main__":
    run_e2e_integration()
