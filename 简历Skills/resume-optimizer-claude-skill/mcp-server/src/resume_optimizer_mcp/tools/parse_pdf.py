"""parse_pdf — extract text from a PDF resume.

Reference implementation. The pattern is:
- one input schema, one output schema, one pure function.
- the function does no I/O beyond reading the file at the given path.
- warnings are surfaced for things the user should know but that aren't errors
  (scanned PDFs, encrypted PDFs that pypdf opened, very long files truncated).
"""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader

from ..schemas import ParsePdfInput, ParsePdfOutput


def parse_pdf(input: ParsePdfInput) -> ParsePdfOutput:
    """Extract text from a PDF.

    Raises:
        FileNotFoundError: the path does not exist.
        ValueError: the file is not a PDF or cannot be opened.
    """
    path = Path(input.path).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")
    if path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a .pdf file, got: {path.suffix}")

    reader = PdfReader(str(path))
    warnings: list[str] = []

    if reader.is_encrypted:
        # pypdf can read most empty-password encrypted PDFs transparently.
        warnings.append(
            "PDF is encrypted; extracted text may be incomplete if a password was required."
        )

    total_pages = len(reader.pages)
    pages_to_read = min(total_pages, input.max_pages)
    if total_pages > input.max_pages:
        warnings.append(
            f"PDF has {total_pages} pages; only the first {input.max_pages} were read."
        )

    chunks: list[str] = []
    for i in range(pages_to_read):
        text = reader.pages[i].extract_text() or ""
        chunks.append(text)

    full = "\n\n".join(chunks).strip()

    if pages_to_read > 0 and not full:
        warnings.append(
            "PDF produced no extractable text — it may be a scanned image. "
            "Consider OCR or pasting the resume text directly."
        )

    return ParsePdfOutput(text=full, pages_read=pages_to_read, warnings=warnings)
