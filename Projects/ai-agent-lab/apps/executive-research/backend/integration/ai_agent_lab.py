import uuid
from runtime.runtime_bootstrap import RuntimeBootstrap
from runtime.models.context import TypedWorkflowContext

class AIAgentLabFacade:
    def __init__(self):
        self.orchestrator = RuntimeBootstrap.build()

    async def execute_research(self, query: str) -> TypedWorkflowContext:
        # Context setup (Application data)
        context = TypedWorkflowContext(
            request_id=str(uuid.uuid4()),
            correlation_id=str(uuid.uuid4()),
            user_request=query
        )
        
        # Use planner to create workflow dynamically
        workflow = self.orchestrator._planner.plan(context)
        
        # Run orchestrator
        self.orchestrator.execute(workflow, context)
        
        return context
