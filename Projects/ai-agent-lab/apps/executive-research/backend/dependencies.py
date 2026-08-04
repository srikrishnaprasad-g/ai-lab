from fastapi import Depends
from integration.ai_agent_lab import AIAgentLabFacade
from app.services.research_service import ResearchService

def get_ai_agent_lab_facade() -> AIAgentLabFacade:
    return AIAgentLabFacade()

def get_research_service(facade: AIAgentLabFacade = Depends(get_ai_agent_lab_facade)) -> ResearchService:
    return ResearchService(facade)
