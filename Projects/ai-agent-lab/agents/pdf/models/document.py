"""Renderer-neutral document domain models."""
from dataclasses import dataclass, field
from datetime import datetime
from abc import ABC
from typing import List

@dataclass
class Metadata:
    title: str
    author: str
    created_at: datetime = field(default_factory=datetime.utcnow)

class ContentElement(ABC):
    """Abstract base class for all document content elements."""
    pass

@dataclass
class Section(ContentElement):
    heading: str
    elements: List[ContentElement]

@dataclass
class Table(ContentElement):
    headers: List[str]
    rows: List[List[str]]

@dataclass
class Paragraph(ContentElement):
    text: str

@dataclass
class Document:
    metadata: Metadata
    content: List[ContentElement]
