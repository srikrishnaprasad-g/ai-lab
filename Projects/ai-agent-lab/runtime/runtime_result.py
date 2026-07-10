"""Runtime result definition."""

from dataclasses import dataclass
from agents.agent_result import AgentResult
from context.request_context import RequestContext


@dataclass
class RuntimeResult:
    """Container for the complete runtime execution state."""

    context: RequestContext
    result: AgentResult
