"""Unit tests for ReportLabGenerator."""
from pathlib import Path
from agents.pdf.reportlab_generator import ReportLabGenerator
from agents.pdf.models.document import Document, Metadata, Paragraph
import os

def test_reportlab_generator_creates_file():
    generator = ReportLabGenerator()
    doc = Document(
        metadata=Metadata(title="Test Doc", author="Test"),
        content=[Paragraph(text="Hello World")]
    )
    output_path = Path("temp_test.pdf")
    
    try:
        result_path = generator.generate(doc, output_path)
        assert result_path.exists()
        assert result_path.name == "temp_test.pdf"
        print("ReportLabGenerator test passed.")
    finally:
        if output_path.exists():
            os.remove(output_path)

if __name__ == "__main__":
    test_reportlab_generator_creates_file()
