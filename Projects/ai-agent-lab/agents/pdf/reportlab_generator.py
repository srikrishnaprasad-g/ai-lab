"""ReportLab implementation of PDFGenerator."""
from pathlib import Path
from agents.pdf.pdf_generator import PDFGenerator
from agents.pdf.models.document import Document, Section, Paragraph, Table
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

class ReportLabGenerator(PDFGenerator):
    """Generates PDFs using ReportLab."""

    def _render_element(self, c, element, y, page_height):
        """Helper to render elements, handling nesting and pagination."""
        margin = 50
        
        if isinstance(element, Section):
            if y < 100:  # If not enough space, new page
                c.showPage()
                y = page_height - margin
                
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y, element.heading)
            y -= 25
            c.setFont("Helvetica", 12)
            for sub_element in element.elements:
                y = self._render_element(c, sub_element, y, page_height)
        elif isinstance(element, Paragraph):
            # Use simpleSplit for basic wrapping
            lines = simpleSplit(element.text, "Helvetica", 12, 450)
            for line in lines:
                if y < margin:
                    c.showPage()
                    y = page_height - margin
                    c.setFont("Helvetica", 12)
                c.drawString(50, y, line)
                y -= 15
        return y

    def generate(self, document: Document, output_path: Path) -> tuple[Path, int]:
        """Generates a PDF file."""
        c = canvas.Canvas(str(output_path), pagesize=letter)
        width, height = letter
        page_count = 1
        
        y = height - 50
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, document.metadata.title)
        y -= 30
        
        c.setFont("Helvetica", 12)
        
        # Override showPage to track page count
        def _showPage():
            nonlocal page_count
            c.showPage()
            page_count += 1
            
        # Re-define _render_element to use _showPage
        def _render_element_with_pagination(c, element, y, page_height):
            margin = 50
            if isinstance(element, Section):
                if y < 100:
                    _showPage()
                    y = page_height - margin
                
                # Add extra spacing before heading
                y -= 15
                
                c.setFont("Helvetica-Bold", 14)
                c.drawString(50, y, element.heading)
                y -= 25
                c.setFont("Helvetica", 12)
                for sub_element in element.elements:
                    y = _render_element_with_pagination(c, sub_element, y, page_height)
            elif isinstance(element, Paragraph):
                lines = simpleSplit(element.text, "Helvetica", 12, 450)
                for line in lines:
                    if y < margin:
                        _showPage()
                        y = page_height - margin
                        c.setFont("Helvetica", 12)
                    c.drawString(50, y, line)
                    y -= 15
            return y

        for element in document.content:
            y = _render_element_with_pagination(c, element, y, height)
            
        c.save()
        return output_path, page_count
