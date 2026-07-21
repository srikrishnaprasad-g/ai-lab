"""CLI entry point for the Multi-Agent Runtime."""

import argparse
import sys
import uuid
from runtime.runtime_bootstrap import RuntimeBootstrap
from context.request_context import RequestContext
from runtime.exceptions import OrchestrationError

def print_banner(agent, model):
    print("========================================")
    print("         AI Agent Lab Runtime           ")
    print("========================================")
    print(f" Agent: {agent}")
    print(f" Model: {model or 'Default'}")
    print("========================================")

def execute_request(orchestrator, request_text, agent_name):
    context = RequestContext(request_id=str(uuid.uuid4()), correlation_id=str(uuid.uuid4()), user_request=request_text)
    
    def callback(ctx: RequestContext) -> str:
        agent = orchestrator.get_agent(agent_name)
        result = agent.execute(ctx)
        return result.output
        
    return orchestrator.execute(context, callback)

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
        orchestrator = RuntimeBootstrap.build()
        
        if args.prompt:
            # One-shot mode
            try:
                print(execute_request(orchestrator, args.prompt, args.agent))
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
                        
                    print(execute_request(orchestrator, normalized_input, args.agent))
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
