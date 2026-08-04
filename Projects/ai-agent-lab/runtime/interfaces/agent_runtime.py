from abc import ABC, abstractmethod
from typing import Any, Dict

class AgentRuntime(ABC):
    @abstractmethod
    async def generate(self, query: str) -> Dict[str, Any]:
        pass
