# LLM Response Contract

This document defines the contract between the platform (SummaryAgent) and LLM providers for structured data generation.

## Overview
To ensure automated PDF report generation, all summarization LLM responses MUST adhere to a strict JSON format.

## JSON Schema

The LLM MUST return a valid JSON object matching this schema:

```json
{
  "executive_summary": "string (200-300 words)",
  "key_findings": [
    {
      "title": "string",
      "description": "string (40-100 words)",
      "importance": "High"
    }
  ],
  "knowledge_gaps": [
    {
      "question": "string",
      "reason": "string"
    }
  ],
  "overall_confidence": "High"
}
```

## Validation Rules

The `SummaryAgent` enforces the following validation:

1.  **Format:** Must be parseable as valid JSON.
2.  **Required Fields:** `executive_summary` and `key_findings` must be present.
3.  **Finding Structure:** Each finding in `key_findings` must contain `title`, `description`, and `importance`.
4.  **Handling Non-JSON:** If the model returns markdown code fences or conversational text, the `SummaryAgent` attempts to extract the JSON object using regex.

## Failure Modes

- **Parsing Failure:** If JSON is malformed or extraction fails, the agent reports `AgentResult(success=False, ...)`.
- **Contract Violation:** If required fields are missing, the agent rejects the response as invalid.

## Schema Evolution
- Any changes to this schema must be reflected in `prompts/templates.py` and `agents/summary/summary_agent.py` parsing logic.
