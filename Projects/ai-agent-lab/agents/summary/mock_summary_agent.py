"""Mock summary agent implementation."""

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from agents.agent import Agent
from agents.agent_result import AgentResult
from context.execution_event import ExecutionEvent
from context import keys
from llm.llm_provider import LLMProvider
from llm.llm_request import LLMRequest
from prompts.prompt_builder import PromptBuilder

if TYPE_CHECKING:
    from context.request_context import RequestContext


class MockSummaryAgent(Agent):
    """A mock implementation of a summary agent using an LLM provider and prompt builder."""

    def __init__(self, llm_provider: LLMProvider, default_model: str, prompt_builder: PromptBuilder) -> None:
        """Initializes the agent with an LLM provider, default model, and prompt builder.

        Args:
            llm_provider: The LLM provider to use for summarization.
            default_model: The default LLM model to use.
            prompt_builder: The prompt builder to use for summarization.
        """
        self._llm_provider = llm_provider
        self._default_model = default_model
        self._prompt_builder = prompt_builder

    def name(self) -> str:
        """Gets the name of the agent."""
        return "mock_summary_agent"

    def description(self) -> str:
        """Gets a brief description of the agent."""
        return "A mock summary agent that processes search results via LLM and prompt builder."

    def execute(self, context: "RequestContext") -> AgentResult:
        """Executes the summarization process using LLM."""
        # Read search response
        search_response = context.working_memory.get(keys.SEARCH_RESPONSE)
        if not search_response:
             raise AgentExecutionError("SearchResponse missing from RequestContext.")
        
        # Build prompt using PromptBuilder
        prompt_result = self._prompt_builder.build(search_response)

        # Call LLM
        # TODO:
        # Pass PromptResult.system_prompt to LLMRequest
        # once provider interfaces support system prompts.
        response = self._llm_provider.generate(
            LLMRequest(
                prompt=prompt_result.prompt, 
                model=self._default_model
            )
        )

        # Store summary in memory
        summary = response.content
        context.working_memory[keys.FINAL_SUMMARY] = summary

        # Append execution event
        event = ExecutionEvent(
            event_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            component=self.name(),
            component_type="agent",
            event_type="completed",
            details={
                "provider": response.provider,
                "model": response.model,
                "summary_length": len(summary)
            },
            duration_ms=0.0
        )
        context.execution_trace.append(event)

        return AgentResult(
            success=True,
            output=summary,
            metadata={
                "agent": self.name(),
                "source": "mock",
                "documents": len(search_response.results)
            }
        )
