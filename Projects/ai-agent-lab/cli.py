"""CLI entry point for the Multi-Agent Runtime."""

import argparse
import sys
import uuid
import logging
import time
from datetime import datetime, timezone, timedelta
from runtime.runtime_bootstrap import RuntimeBootstrap
from config.settings import load_settings
from context.request_context import RequestContext
from runtime.exceptions import OrchestrationError
from runtime.models.context import TypedWorkflowContext
from agents.summary.models.core import SummaryResult
from agents.pdf.models.pdf_result import PDFResult

# Configure logging for the pipeline
logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger("pipeline")

def print_banner(agent, provider, model):
    print("═══════════════════════════════════════════════")
    print("            AI Agent Lab Runtime           ")
    print("═══════════════════════════════════════════════")
    print(f"Agent      : {agent}")
    print(f"Provider   : {provider.capitalize() if provider else 'Unknown'}")
    print(f"Model      : {model if model else 'Unknown'}")
    print("═══════════════════════════════════════════════")

def print_trace_header(prompt):
    print("=================================================")
    print("AI Agent Lab Production Trace")
    print("=================================================")
    print(f"\nRequest:\n{prompt}\n")

def print_verbose_trace(context, total_time):
    # Fetch results from context
    research_res = context.working_memory.get("research_result")
    summary_metrics = context.working_memory.get("summary_metrics") or {}
    pdf_res = context.working_memory.get("final_result")
    
    print("\n================================================")
    print("Runtime")
    print("================================================")
    print(f"Request ID : {context.request_id}")
    print(f"Correlation ID : {context.correlation_id}")
    print(f"Provider   : {summary_metrics.get('provider', 'N/A').capitalize()}")
    print(f"Model      : {summary_metrics.get('model', 'N/A')}")
    
    print("\n================================================")
    print("Research")
    print("================================================")
    if research_res:
        print(f"Search Provider : {research_res.search_provider}")
        print(f"Result Count    : {research_res.source_count}")
        print(f"Latency         : {research_res.processing_duration:.2f} s")
    else:
        print("Research Phase Skipped or Failed")
        
    print("\n================================================")
    print("Summarization")
    print("================================================")
    if summary_metrics:
        print(f"Prompt Length   : {summary_metrics.get('prompt_length')} chars")
        print(f"HTTP Status     : {summary_metrics.get('status_code')}")
        print(f"Latency         : {summary_metrics.get('latency'):.2f} s")
        print(f"Response Length : {summary_metrics.get('response_length')} chars")
    else:
        print("Summarization Phase Skipped or Failed")
        
    print("\n================================================")
    print("PDF")
    print("================================================")
    if pdf_res:
        print(f"Page Count      : {pdf_res.page_count}")
        print(f"File Path       : {pdf_res.file_path}")
    else:
        print("PDF Phase Skipped or Failed")
        
    print("\n================================================")
    print("Pipeline Summary")
    print("================================================")
    print(f"Total Runtime   : {total_time:.2f} s")
    print(f"Status          : SUCCESS")
    print("================================================\n")

def print_final_output(summary_result, pdf_result):
    if summary_result:
        print("\n═══════════════════════════════════════")
        print("EXECUTIVE SUMMARY")
        print("═══════════════════════════════════════")
        print(summary_result.executive_summary)
        
        print("\n═══════════════════════════════════════")
        print("KEY FINDINGS")
        print("═══════════════════════════════════════")
        for i, finding in enumerate(summary_result.key_findings, 1):
            print(f"{i}. {finding.title}")
            print(f"Importance: {finding.importance.value}")
            print(f"{finding.description}\n")

    if pdf_result:
        # Convert UTC (assuming generation_time is UTC naive) to IST (UTC+5:30)
        ist_offset = timedelta(hours=5, minutes=30)
        ist_tz = timezone(ist_offset)
        # Assume naive datetime is UTC
        utc_dt = pdf_result.generation_time.replace(tzinfo=timezone.utc)
        ist_dt = utc_dt.astimezone(ist_tz)
        
        print("\n═══════════════════════════════════════")
        print("PDF GENERATED")
        print("═══════════════════════════════════════")
        print(f"File: {pdf_result.file_path}")
        print(f"Page Count: {pdf_result.page_count}")
        print(f"Generation Time: {ist_dt.strftime('%Y-%m-%d %H:%M:%S %Z')}")

def execute_request(orchestrator, request_text):
    # Using TypedWorkflowContext as required by RuntimeOrchestrator
    context = TypedWorkflowContext(
        request_id=str(uuid.uuid4()), 
        correlation_id=str(uuid.uuid4()), 
        user_request=request_text
    )
    
    # We need to use the planner to create the workflow definition
    workflow = orchestrator._planner.plan(context)
        
    result = orchestrator.execute(workflow, context)
    return result, context

def main():
    parser = argparse.ArgumentParser(description="AI Agent Lab Runtime CLI")
    parser.add_argument("prompt", nargs="?", help="One-shot prompt to execute")
    parser.add_argument("--version", action="version", version="1.0.0")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--agent", default="research_agent", help="Agent to use (default: research_agent)")
    parser.add_argument("--model", help="Model to use (Not implemented yet)")
    
    args = parser.parse_args()
    settings = load_settings()
    
    if args.model:
        print("Warning: --model is not implemented yet. Using default model.", file=sys.stderr)

    try:
        if args.verbose:
            logger.setLevel(logging.DEBUG)
            print_trace_header(args.prompt)
            start_time = time.perf_counter()
            
            try:
                # Instrumented Execution
                orchestrator = RuntimeBootstrap.build()
                
                # 1. CLI
                print(f"[PASS] CLI (0 ms)")
                
                if not args.prompt:
                    print("[WARN] No prompt provided. Exiting.")
                    sys.exit(0)
                
                # 2. Planner
                start = time.perf_counter()
                context = TypedWorkflowContext(
                    request_id=str(uuid.uuid4()), 
                    correlation_id=str(uuid.uuid4()), 
                    user_request=args.prompt
                )
                workflow = orchestrator._planner.plan(context)
                print(f"[PASS] Planner ({int((time.perf_counter() - start) * 1000)} ms)")
                
                # 3. Execution via Orchestrator
                result = orchestrator.execute(workflow, context)
                
                total_time = time.perf_counter() - start_time
                print_verbose_trace(context, total_time)
                
            except Exception as e:
                print(f"\n[FAIL] Pipeline halted.\nReason: {e}")
        else:
            orchestrator = RuntimeBootstrap.build()
            
            if args.prompt:
                # One-shot mode
                try:
                    result, context = execute_request(orchestrator, args.prompt)
                    print_final_output(context.get("summary_result", SummaryResult), context.get("final_result", PDFResult))
                except OrchestrationError as e:
                    print(f"Runtime Error: {e}", file=sys.stderr)
                    sys.exit(1)
            else:
                # Interactive mode
                print_banner(args.agent, settings.default_llm_provider, settings.default_llm_model)
                print("Interactive Mode. Type EXIT or QUIT to finish.")
                
                while True:
                    try:
                        user_input = input("AI> ")
                        normalized_input = user_input.lstrip('\ufeff').strip()
                        if normalized_input.upper() in ["EXIT", "QUIT"]:
                            print("Goodbye!")
                            break
                        if not normalized_input:
                            continue
                            
                        result, context = execute_request(orchestrator, normalized_input)
                        print_final_output(context.get("summary_result", SummaryResult), context.get("final_result", PDFResult))
                    except (KeyboardInterrupt, EOFError):
                        print("\nGoodbye!")
                        break
                    except OrchestrationError as e:
                        print(f"Runtime Error: {e}", file=sys.stderr)
                        
    except Exception as e:
        print(f"Unexpected Internal Error: {e}", file=sys.stderr)
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    main()
