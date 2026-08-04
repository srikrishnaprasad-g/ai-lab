from runtime.interfaces.agent_runtime import AgentRuntime
from typing import Any, Dict

class WorkflowEngine:
    def __init__(self, runtime: AgentRuntime):
        self.runtime = runtime

    async def execute(self, query: str) -> Dict[str, Any]:
        return await self.runtime.generate(query)
