"""Enums for Summary Framework."""

from enum import Enum

class ImportanceLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class ConfidenceLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    UNKNOWN = "UNKNOWN"

class SummaryStyle(Enum):
    EXECUTIVE = "EXECUTIVE"
    TECHNICAL = "TECHNICAL"
    BUSINESS = "BUSINESS"
    DETAILED = "DETAILED"

class Audience(Enum):
    EXECUTIVE = "EXECUTIVE"
    PRODUCT = "PRODUCT"
    ENGINEERING = "ENGINEERING"
    CUSTOMER = "CUSTOMER"

class Tone(Enum):
    NEUTRAL = "NEUTRAL"
    FORMAL = "FORMAL"
    CONCISE = "CONCISE"

class OutputFormat(Enum):
    MARKDOWN = "MARKDOWN"
    TEXT = "TEXT"
    JSON = "JSON"
