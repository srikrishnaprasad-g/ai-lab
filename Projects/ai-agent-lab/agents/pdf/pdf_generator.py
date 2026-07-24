"""Abstract PDF generator interface."""
from abc import ABC, abstractmethod
from pathlib import Path
from agents.pdf.models.document import Document

class PDFGenerator(ABC):
    """Interface for document rendering."""
    
    @abstractmethod
    def generate(self, document: Document, output_path: Path) -> tuple[Path, int]:
        """Generates a PDF file from a Document model."""
        pass
