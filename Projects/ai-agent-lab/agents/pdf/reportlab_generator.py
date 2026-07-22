"""ReportLab implementation of PDFGenerator."""
from pathlib import Path
from agents.pdf.pdf_generator import PDFGenerator
from agents.pdf.models.document import Document, Section, Paragraph, Table
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportLabGenerator(PDFGenerator):
    """Generates PDFs using ReportLab."""
    
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
            if isinstance(element, Paragraph):
                c.drawString(50, y, element.text)
                y -= 20
            # Tables and Sections can be expanded here
            
        c.save()
        return output_path
