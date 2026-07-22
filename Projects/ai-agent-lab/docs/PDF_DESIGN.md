# PDF Agent Design

## Purpose
The PDF Agent converts structured `SummaryResult` domain objects into professional PDF documents.

## Architecture
- `PDFAgent`: Orchestrates the mapping of domain objects to document models and triggers generation.
- `PDFGenerator` (Interface): Abstract contract for document rendering (provider pattern).
- `ReportLabGenerator`: Concrete rendering provider using ReportLab.
- `Document` (Domain Model): Renderer-neutral document structure (Metadata, Sections, Elements).

## Rendering Flow
1. `SummaryAgent` completes work -> `SummaryResult` in `RequestContext`.
2. `PDFAgent` is invoked via `RuntimeOrchestrator`.
3. `PDFAgent` maps `SummaryResult` -> `Document` domain model.
4. `PDFAgent` invokes `PDFGenerator.generate(Document, Path)`.
5. `PDFGenerator` (e.g., ReportLab) renders the document to a file.
6. `PDFAgent` returns `PDFResult` containing the file path and metadata.

## Extensibility
- **Content Types:** `Document` uses `ContentElement` subclasses (e.g., `Paragraph`, `Table`). Adding new types (e.g., `ImageElement`) only requires extending the `ContentElement` hierarchy and updating the generator implementation.
- **Formats:** New output formats (e.g., DOCX) can be supported by implementing new `PDFGenerator` interfaces.

## Design Principles
- **Separation of Concerns:** `PDFAgent` handles mapping, `PDFGenerator` handles rendering.
- **Dependency Isolation:** `ReportLab` is completely hidden behind the `PDFGenerator` interface.
- **DI:** Generator is injected via `AgentFactory` / `RuntimeBootstrap`.
