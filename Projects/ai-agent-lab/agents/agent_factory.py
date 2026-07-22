"""Factory for production agents."""

from agents.research_agent import ResearchAgent
from agents.summary.summary_agent import SummaryAgent
from agents.pdf.pdf_agent import PDFAgent
from agents.pdf.pdf_generator import PDFGenerator
from prompts.prompt_registry import PromptRegistry
from prompts.summary_prompt_builder import SummaryPromptBuilder
from search.search_service import SearchService
from observability.telemetry_service import TelemetryService

class AgentFactory:
    """Factory for creating production-ready agents."""

    def __init__(
        self, 
        telemetry_service: TelemetryService, 
        search_service: SearchService, 
        prompt_registry: PromptRegistry,
        pdf_generator: PDFGenerator
    ) -> None:
        """Initializes the agent factory."""
        self._telemetry_service = telemetry_service
        self._search_service = search_service
        self._prompt_registry = prompt_registry
        self._pdf_generator = pdf_generator

    def create_research_agent(self) -> ResearchAgent:
        """Creates a new ResearchAgent."""
        return ResearchAgent(self._telemetry_service, self._search_service)
        
    def create_summary_agent(self) -> SummaryAgent:
        """Creates a new SummaryAgent."""
        prompt_builder = SummaryPromptBuilder(self._prompt_registry)
        return SummaryAgent(self._telemetry_service, prompt_builder)
        
    def create_pdf_agent(self) -> PDFAgent:
        """Creates a new PDFAgent."""
        return PDFAgent(self._telemetry_service, self._pdf_generator)
