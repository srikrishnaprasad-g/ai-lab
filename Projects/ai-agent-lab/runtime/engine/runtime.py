from runtime.interfaces.agent_runtime import AgentRuntime
from typing import Any, Dict
import uuid

class MockAgentRuntime(AgentRuntime):
    async def generate(self, query: str) -> Dict[str, Any]:
        return {
            "executive_summary": f"Mocked summary for: {query[:20]}...",
            "key_insights": ["Insight A", "Insight B"],
            "report_id": str(uuid.uuid4())
        }
