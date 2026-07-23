"""CLI entry point for the Multi-Agent Runtime."""

import argparse
import sys
import uuid
import logging
import time
from runtime.runtime_bootstrap import RuntimeBootstrap
from context.request_context import RequestContext
from runtime.exceptions import OrchestrationError
from runtime.models.context import TypedWorkflowContext

# Configure logging for the pipeline
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("pipeline")

def print_banner(agent, model):
    print("========================================")
    print("         AI Agent Lab Runtime           ")
    print("========================================")
    print(f" Agent: {agent}")
    print(f" Model: {model or 'Default'}")
    print("========================================")

def print_trace_header(prompt):
    print("=================================================")
    print("AI Agent Lab Production Trace")
    print("=================================================")
    print(f"\nRequest:\n{prompt}\n")

def print_trace_footer(total_time, status):
    print("\n=================================================")
    print(f"Pipeline Status:\n{status}")
    print(f"Total Time:\n{total_time:.1f} sec")
    print("=================================================")

def execute_request(orchestrator, request_text):
    # Using TypedWorkflowContext as required by RuntimeOrchestrator
    context = TypedWorkflowContext(
        request_id=str(uuid.uuid4()), 
        correlation_id=str(uuid.uuid4()), 
        user_request=request_text
    )
    
    # We need to use the planner to create the workflow definition
    workflow = orchestrator._planner.plan(context)
        
    return orchestrator.execute(workflow, context)

def main():
    parser = argparse.ArgumentParser(description="AI Agent Lab Runtime CLI")
    parser.add_argument("prompt", nargs="?", help="One-shot prompt to execute")
    parser.add_argument("--version", action="version", version="1.0.0")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--agent", default="research_agent", help="Agent to use (default: research_agent)")
    parser.add_argument("--model", help="Model to use (Not implemented yet)")
    
    args = parser.parse_args()
    
    if args.model:
        print("Warning: --model is not implemented yet. Using default model.", file=sys.stderr)

    try:
        if args.verbose:
            print_trace_header(args.prompt)
            start_time = time.perf_counter()
            
            try:
                # Instrumented Execution
                orchestrator = RuntimeBootstrap.build()
                
                # 1. CLI
                print(f"[PASS] CLI (0 ms)")
                
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
                print_trace_footer(total_time, "PASS")
                print(result)
                
            except Exception as e:
                print(f"\n[FAIL] Pipeline halted.\nReason: {e}")
        else:
            orchestrator = RuntimeBootstrap.build()
            
            if args.prompt:
                # One-shot mode
                try:
                    print(execute_request(orchestrator, args.prompt))
                except OrchestrationError as e:
                    print(f"Runtime Error: {e}", file=sys.stderr)
                    sys.exit(1)
            else:
                # Interactive mode
                print_banner(args.agent, args.model)
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
                            
                        print(execute_request(orchestrator, normalized_input))
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
