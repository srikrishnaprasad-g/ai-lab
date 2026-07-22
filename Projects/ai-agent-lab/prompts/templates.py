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
    version="1.0",
    template_string="""You are an expert analyst. Your task is to provide a concise, factual, and professional summary based ONLY on the provided search results.
    Rules:
    - Cite sources using [1], [2], etc.
    - If sources conflict, explicitly identify the conflict and cite evidence.
    - If information is missing, state 'Information not found'.
    - Do not make assumptions or guess.""",
    required_variables=set()
)

SUMMARIZATION_USER_V1 = PromptTemplate(
    template_id="summarization_user_v1",
    description="User prompt for summary agent",
    version="1.0",
    template_string="""Summarize the topic: {topic}.
    Tone: {tone}
    Context: {context}

    Search Results:
    {search_results}
    """,
    required_variables={"topic", "search_results", "tone", "context"}
)

WRITING_TEMPLATE = PromptTemplate(
    template_id="writing_task",
    description="Template for writing tasks",
    version="1.0",
    template_string="Write a {document_type} about {subject}. Tone: {tone}.",
    required_variables={"document_type", "subject", "tone"}
)
