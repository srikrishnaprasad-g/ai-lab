"""ReportLab implementation of PDFGenerator."""
from pathlib import Path
from agents.pdf.pdf_generator import PDFGenerator
from agents.pdf.models.document import Document, Section, Paragraph, Table
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

class ReportLabGenerator(PDFGenerator):
    """Generates PDFs using ReportLab."""

    def _render_element(self, c, element, y):
        """Helper to render elements, handling nesting."""
        if isinstance(element, Section):
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y, element.heading)
            y -= 25
            c.setFont("Helvetica", 12)
            for sub_element in element.elements:
                y = self._render_element(c, sub_element, y)
        elif isinstance(element, Paragraph):
            # Use simpleSplit for basic wrapping
            lines = simpleSplit(element.text, "Helvetica", 12, 450)
            for line in lines:
                c.drawString(50, y, line)
                y -= 15
        return y

    def generate(self, document: Document, output_path: Path) -> Path:
        """Generates a PDF file."""
        c = canvas.Canvas(str(output_path), pagesize=letter)
        width, height = letter
        
        y = height - 50
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, document.metadata.title)
        y -= 30
        
        c.setFont("Helvetica", 12)
        for element in document.content:
            y = self._render_element(c, element, y)
            
        c.save()
        return output_path
