from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from app.schemas.research import ResearchRequest, ResearchResponse
from app.services.research_service import ResearchService
from dependencies import get_research_service
from app.core.responses import ApiResponse
from app.config.settings import settings
import os

router = APIRouter()

@router.post("/research", response_model=ApiResponse[ResearchResponse])
async def generate_report(
    request: ResearchRequest,
    research_service: ResearchService = Depends(get_research_service)
):
    result = await research_service.generate_report(request)
    return ApiResponse(data=result)

@router.get("/download/{filename}")
async def download_report(filename: str):
    # Use the absolute path derived from the environment variable (or config)
    report_dir = os.getenv("REPORT_DIR")
    if not report_dir:
        return {"status": "error", "message": "REPORTS_DIR not configured"}
        
    file_path = os.path.join(report_dir, filename)
    if not os.path.exists(file_path):
        return {"status": "error", "message": f"File not found at {file_path}"}
    return FileResponse(file_path, media_type='application/pdf', filename=filename)

