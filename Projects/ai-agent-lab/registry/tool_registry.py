"""Tool registry implementation."""

from tools.tool import Tool
from registry.registry import Registry


class ToolRegistry(Registry[Tool]):
    """Registry specifically for Tool components."""
    pass
