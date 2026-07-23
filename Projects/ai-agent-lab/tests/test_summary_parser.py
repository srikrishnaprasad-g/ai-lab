import pytest
import json
from agents.summary.llm_response_parser import LLMResponseParser
from agents.summary.models.enums import ImportanceLevel

def test_valid_json():
    content = """{
      "executive_summary": "Summary content.",
      "key_findings": [
        {
          "title": "Finding 1",
          "description": "Description 1",
          "importance": "High"
        }
      ]
    }"""
    result = LLMResponseParser.parse_and_validate(content)
    assert result.executive_summary == "Summary content."
    assert len(result.key_findings) == 1
    assert result.key_findings[0].title == "Finding 1"
    assert result.key_findings[0].importance == ImportanceLevel.HIGH

def test_markdown_wrapped_json():
    content = """```json
    {
      "executive_summary": "Summary content.",
      "key_findings": []
    }
    ```"""
    result = LLMResponseParser.parse_and_validate(content)
    assert result.executive_summary == "Summary content."

def test_malformed_json():
    content = "{ invalid json }"
    with pytest.raises(ValueError, match="Failed to parse LLM response"):
        LLMResponseParser.parse_and_validate(content)

def test_missing_fields():
    content = '{"executive_summary": "Missing findings"}'
    with pytest.raises(ValueError, match="Missing required fields"):
        LLMResponseParser.parse_and_validate(content)

def test_malformed_finding():
    content = """{
      "executive_summary": "Summary",
      "key_findings": [{"title": "Incomplete"}]
    }"""
    with pytest.raises(ValueError, match="Malformed key finding structure"):
        LLMResponseParser.parse_and_validate(content)
