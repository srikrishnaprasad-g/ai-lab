"""PDF Agent result domain model."""
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List

@dataclass
class PDFResult:
    file_path: Path
    format: str = "pdf"
    generation_time: datetime = field(default_factory=datetime.utcnow)
    warnings: List[str] = field(default_factory=list)
    page_count: int = 0
