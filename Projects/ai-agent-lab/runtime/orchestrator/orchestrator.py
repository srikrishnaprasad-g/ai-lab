"""Orchestrator implementation."""
from typing import Optional, Any
from runtime.orchestrator.task_graph import TaskGraph
from runtime.models.workflow import WorkflowDefinition
from runtime.models.context import TypedWorkflowContext
from registry.agent_registry import AgentRegistry
from runtime.pipeline.execution_pipeline import ExecutionPipeline
from agents.summary.models.summary_request import SummaryRequest
from agents.summary.models.core import SummaryResult
from agents.summary.models.enums import SummaryStyle, Audience, Tone, OutputFormat
from agents.pdf.models.pdf_result import PDFResult
from agents.research.research_result import ResearchResult

import time
import logging

logger = logging.getLogger("pipeline")

class RuntimeOrchestrator:
    """Manages agent execution lifecycle."""
    
    def __init__(self, planner: Any, pipeline: ExecutionPipeline, registry: AgentRegistry) -> None:
        self._planner = planner
        self._registry = registry
        self._pipeline = pipeline
        
    def execute(self, workflow: WorkflowDefinition, context: TypedWorkflowContext) -> Any:
        """Executes a workflow."""
        completed_tasks = []
        
        while True:
            executable = workflow.task_graph.get_executable_tasks(completed_tasks)
            if not executable:
                break
                
            # Sequential execution for now
            task_id = executable[0]
            agent = self._registry.get(task_id)
            
            # Context-driven input preparation (Task 6.5A-R Recommendation)
            if task_id == "summary_agent":
                research_result = context.working_memory.get("research_result")
                if isinstance(research_result, ResearchResult):
                    # Construct SummaryRequest for SummaryAgent
                    req = SummaryRequest(
                        research_result=research_result,
                        summary_style=SummaryStyle.EXECUTIVE,
                        audience=Audience.EXECUTIVE,
                        tone=Tone.FORMAL,
                        length="medium",
                        output_format=OutputFormat.MARKDOWN
                    )
                    context.set("summary_request", req)
            
            # Execute Pipeline
            start = time.perf_counter()
            try:
                result = self._pipeline.execute(agent.execute, context)
                if not result.success:
                    logger.info(f"[FAIL] {task_id.replace('_', ' ').title()}")
                    return None
            except Exception as e:
                logger.info(f"[FAIL] {task_id.replace('_', ' ').title()}\nReason: {e}")
                raise
            
            duration = (time.perf_counter() - start) * 1000
            logger.info(f"[PASS] {task_id.replace('_', ' ').title()} ({int(duration)} ms)")
            
            # Context-driven output propagation (Task 6.5A-R Recommendation)
            if result.success and result.output is not None:
                if task_id == "research_agent":
                    context.set("research_result", result.output)
                    logger.info(f"[PASS] Tavily\nResults: {len(result.output.sources)}")
                elif task_id == "summary_agent":
                    context.set("summary_result", result.output)
                    logger.info(f"[PASS] Summary Agent\nFindings: {len(result.output.key_findings)}")
                elif task_id == "pdf_agent":
                    context.set("final_result", result.output)
                    logger.info(f"[PASS] PDF Agent\nSections: 2")
            
            completed_tasks.append(task_id)
            
        return context.get("final_result", Any)

