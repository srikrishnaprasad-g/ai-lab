"""Mock PDF generator for testing/environment constraints."""
from pathlib import Path
from agents.pdf.pdf_generator import PDFGenerator
from agents.pdf.models.document import Document

class MockPDFGenerator(PDFGenerator):
    """Mock generator that does not require ReportLab."""
    
    def generate(self, document: Document, output_path: Path) -> Path:
        """Simulates PDF generation by creating a dummy file."""
        with open(output_path, "w") as f:
            f.write(f"Mock PDF content for {document.metadata.title}")
        return output_path
