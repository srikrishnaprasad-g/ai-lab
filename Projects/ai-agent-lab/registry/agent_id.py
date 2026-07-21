"""Agent registry identifiers."""

from enum import StrEnum


class AgentId(StrEnum):
    """Enumeration of available agent identifiers."""

    ROOT = "root"
    RESEARCH = "mock_research_agent"
    SUMMARY = "mock_summary_agent"
