"""Agent registry implementation."""

from agents.agent import Agent
from registry.registry import Registry


class AgentRegistry(Registry[Agent]):
    """Registry specifically for Agent components."""
    pass
