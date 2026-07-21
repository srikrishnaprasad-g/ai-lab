"""Unit tests for the Prompt Framework."""
from prompts.prompt_registry import PromptRegistry
from prompts.prompt_builder import DefaultPromptBuilder
from prompts.templates import RESEARCH_TEMPLATE, SUMMARIZATION_TEMPLATE, WRITING_TEMPLATE

def test_registry_registration():
    registry = PromptRegistry()
    registry.register(RESEARCH_TEMPLATE)
    assert registry.get("research_task") == RESEARCH_TEMPLATE

def test_registry_duplicate_prevention():
    registry = PromptRegistry()
    registry.register(RESEARCH_TEMPLATE)
    try:
        registry.register(RESEARCH_TEMPLATE)
        assert False, "Should have raised ValueError for duplicate registration"
    except ValueError:
        pass

def test_builder_rendering():
    registry = PromptRegistry()
    registry.register(RESEARCH_TEMPLATE)
    builder = DefaultPromptBuilder(registry)
    
    rendered = builder.build("research_task", {"topic": "AI Agents", "format": "markdown"})
    assert "Research the following topic: AI Agents" in rendered
    assert "Provide a summary in markdown." in rendered

def test_builder_missing_variables():
    registry = PromptRegistry()
    registry.register(RESEARCH_TEMPLATE)
    builder = DefaultPromptBuilder(registry)
    
    try:
        builder.build("research_task", {"topic": "AI Agents"})
        assert False, "Should have raised ValueError for missing variables"
    except ValueError as e:
        assert "Missing required variables" in str(e)

if __name__ == "__main__":
    test_registry_registration()
    test_registry_duplicate_prevention()
    test_builder_rendering()
    test_builder_missing_variables()
    print("All prompt framework tests PASSED.")
