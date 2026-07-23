"""Task topology definitions."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class TaskNode:
    """A single node in the execution graph."""
    agent_id: str
    dependencies: List[str] = field(default_factory=list)
    config: Dict[str, Any] = field(default_factory=dict)

class TaskGraph:
    """Defines execution order and dependencies."""
    
    def __init__(self) -> None:
        self.nodes: Dict[str, TaskNode] = {}
        
    def add_task(self, node: TaskNode) -> None:
        self.nodes[node.agent_id] = node
        
    def get_executable_tasks(self, completed_tasks: List[str]) -> List[str]:
        """Returns tasks whose dependencies are met."""
        executable = []
        for agent_id, node in self.nodes.items():
            if agent_id not in completed_tasks and all(dep in completed_tasks for dep in node.dependencies):
                executable.append(agent_id)
        return executable
