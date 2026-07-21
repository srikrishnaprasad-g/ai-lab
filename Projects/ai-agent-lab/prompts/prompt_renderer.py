"""Prompt renderer."""
from prompts.prompt_template import PromptTemplate
from prompts.prompt_variables import PromptVariables

class PromptRenderer:
    """Renders prompt templates with provided variables."""
    
    def render(self, template: PromptTemplate, variables: PromptVariables) -> str:
        """Renders the template with variables."""
        variables.validate(template.required_variables)
        return template.template_string.format(**variables.get_all())
