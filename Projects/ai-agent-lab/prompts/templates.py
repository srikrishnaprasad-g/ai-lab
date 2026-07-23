"""Prompt templates."""
from prompts.prompt_template import PromptTemplate

RESEARCH_TEMPLATE = PromptTemplate(
    template_id="research_task",
    description="Template for research tasks",
    version="1.0",
    template_string="Research the following topic: {topic}. Provide a summary in {format}.",
    required_variables={"topic", "format"}
)

SUMMARIZATION_SYSTEM_V1 = PromptTemplate(
    template_id="summarization_system_v1",
    description="System prompt for summary agent",
    version="3.0",
    template_string="""You are an expert research analyst.
    
    Synthesize the provided search results into a professional executive research report.
    
    Return ONLY valid JSON.
    
    JSON Schema:
    {{
      "executive_summary": "200-300 word analytical synthesis of the topic, its importance, trends, and limitations.",
      "key_findings": [
        {{
          "title": "Title",
          "description": "40-100 word detailed analytical finding",
          "importance": "High"
        }}
      ]
    }}
    
    Do not add markdown, conversational text, or explanations. Only the JSON.""",
    required_variables=set()
)

SUMMARIZATION_USER_V1 = PromptTemplate(
    template_id="summarization_user_v1",
    description="User prompt for summary agent",
    version="2.0",
    template_string="""Please generate an executive research report for the topic: {topic}.
    
    Use the following search results as the sole evidence:
    {search_results}
    
    Style Guidelines:
    Tone: {tone}
    Context: {context}""",
    required_variables={"topic", "search_results", "tone", "context"}
)

WRITING_TEMPLATE = PromptTemplate(
    template_id="writing_task",
    description="Template for writing tasks",
    version="1.0",
    template_string="Write a {document_type} about {subject}. Tone: {tone}.",
    required_variables={"document_type", "subject", "tone"}
)
