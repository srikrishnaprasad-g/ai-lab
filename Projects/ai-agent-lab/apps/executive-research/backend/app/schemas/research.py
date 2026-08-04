from pydantic import BaseModel

class KeyInsight(BaseModel):
    title: str
    description: str

class ResearchRequest(BaseModel):
    query: str

class ResearchResponse(BaseModel):
    executive_summary: str
    key_insights: list[KeyInsight]
    report_id: str
