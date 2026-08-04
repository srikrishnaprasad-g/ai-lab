from fastapi import HTTPException
from app.schemas.research import ResearchRequest, ResearchResponse, KeyInsight
from integration.ai_agent_lab import AIAgentLabFacade
from shared.exceptions import ValidationException
from agents.summary.models.core import SummaryResult
from agents.pdf.models.pdf_result import PDFResult

class ResearchService:
    def __init__(self, facade: AIAgentLabFacade):
        self.facade = facade

    async def generate_report(self, request: ResearchRequest) -> ResearchResponse:
        query = request.query.strip()
        if not query:
            raise ValidationException("Query cannot be empty")
        if len(query) > 5000:
            raise ValidationException("Query too long")

        try:
            context = await self.facade.execute_research(query)
            summary_result = context.get("summary_result", SummaryResult)
            pdf_result = context.get("final_result", PDFResult)
            
            # Map findings to ResearchResponse
            return ResearchResponse(
                executive_summary=summary_result.executive_summary,
                key_insights=[KeyInsight(title=f.title, description=f.description) for f in summary_result.key_findings],
                report_id=pdf_result.file_path.name
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
