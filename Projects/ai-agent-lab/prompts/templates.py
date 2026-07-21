"""Prompt templates."""
from prompts.prompt_template import PromptTemplate

RESEARCH_TEMPLATE = PromptTemplate(
    template_id="research_task",
    description="Template for research tasks",
    version="1.0",
    template_string="Research the following topic: {topic}. Provide a summary in {format}.",
    required_variables={"topic", "format"}
)

SUMMARIZATION_TEMPLATE = PromptTemplate(
    template_id="summarization_task",
    description="Template for summarization tasks",
    version="1.0",
    template_string="Summarize the following text: {text}. Focus on {focus_area}.",
    required_variables={"text", "focus_area"}
)

WRITING_TEMPLATE = PromptTemplate(
    template_id="writing_task",
    description="Template for writing tasks",
    version="1.0",
    template_string="Write a {document_type} about {subject}. Tone: {tone}.",
    required_variables={"document_type", "subject", "tone"}
)
