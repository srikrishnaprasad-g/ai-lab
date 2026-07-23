"""Response parsing and validation utilities for LLM responses."""
import json
import re
import logging
from typing import Any, Dict, List, Optional
from agents.summary.models.core import Finding, SummaryResult
from agents.summary.models.enums import ConfidenceLevel, ImportanceLevel

logger = logging.getLogger("pipeline")

class LLMResponseParser:
    """Robust parser for LLM responses."""

    @staticmethod
    def parse_and_validate(content: str) -> SummaryResult:
        """Parses and validates LLM response content."""
        
        # 1. Extraction
        content = content.strip()
        match = re.search(r"(\{.*\})", content, re.DOTALL)
        if match:
            content = match.group(1).strip()
            
        # 2. Decoding
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            logger.error(f"JSON Parsing Error: {e}")
            raise ValueError(f"Failed to parse LLM response: {e}")

        # 3. Contract Validation
        if not isinstance(data, dict):
             raise ValueError("LLM response must be a JSON object")

        if "executive_summary" not in data or "key_findings" not in data:
            logger.error("Contract Validation Failed: Missing required fields")
            raise ValueError("Missing required fields: executive_summary, key_findings")

        # 4. Data Mapping & Validation
        findings = []
        for f in data.get("key_findings", []):
            if not all(k in f for k in ["title", "description", "importance"]):
                logger.error(f"Contract Validation Failed: Malformed finding: {f}")
                raise ValueError(f"Malformed key finding structure: {f}")
                
            findings.append(Finding(
                title=f.get("title"),
                description=f.get("description"),
                importance=ImportanceLevel(f.get("importance").upper()),
                supporting_observations=[], 
                confidence=ConfidenceLevel.HIGH
            ))
        
        return SummaryResult(
            executive_summary=data.get("executive_summary"),
            key_findings=findings,
            knowledge_gaps=[],
            citations=[],
            confidence=ConfidenceLevel.HIGH
        )
