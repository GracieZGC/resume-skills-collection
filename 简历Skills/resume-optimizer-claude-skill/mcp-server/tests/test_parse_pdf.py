"""Tests for the parse_pdf tool.

We construct a minimal PDF on the fly (via pypdf's writer) to avoid checking in
a binary fixture. This keeps the test self-contained and reviewable.
"""

from __future__ import annotations

import io

import pytest
from pypdf import PdfReader, PdfWriter

from resume_optimizer_mcp.schemas import ParsePdfInput
from resume_optimizer_mcp.tools import parse_pdf


def _make_pdf(tmp_path, pages: int = 1) -> str:
    """Write a tiny multi-page PDF and return the path.

    pypdf cannot synthesize text glyphs from scratch, so we generate empty pages.
    parse_pdf is still exercised end-to-end (path validation, page counting,
    empty-text warning); a real fixture would be needed to assert extracted text.
    """
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=612, height=792)
    out = tmp_path / "sample.pdf"
    with out.open("wb") as f:
        writer.write(f)
    return str(out)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_pdf(ParsePdfInput(path="/nonexistent/path/to.pdf"))


def test_wrong_extension(tmp_path):
    txt = tmp_path / "not_a_pdf.txt"
    txt.write_text("hello")
    with pytest.raises(ValueError, match="Expected a .pdf"):
        parse_pdf(ParsePdfInput(path=str(txt)))


def test_blank_pdf_warns(tmp_path):
    path = _make_pdf(tmp_path, pages=2)
    result = parse_pdf(ParsePdfInput(path=path))
    assert result.pages_read == 2
    # Blank pages produce no text — the tool should surface this as a warning,
    # so the host can hint the user to OCR or paste text instead.
    assert any("scanned image" in w for w in result.warnings)


def test_max_pages_truncates(tmp_path):
    path = _make_pdf(tmp_path, pages=5)
    result = parse_pdf(ParsePdfInput(path=path, max_pages=2))
    assert result.pages_read == 2
    assert any("only the first 2" in w for w in result.warnings)


def test_max_pages_bounds():
    # max_pages must be in [1, 50] per the schema.
    with pytest.raises(ValueError):
        ParsePdfInput(path="x.pdf", max_pages=0)
    with pytest.raises(ValueError):
        ParsePdfInput(path="x.pdf", max_pages=51)


def test_output_round_trips(tmp_path):
    path = _make_pdf(tmp_path, pages=1)
    result = parse_pdf(ParsePdfInput(path=path))
    # Output is a Pydantic model; model_dump() should be JSON-serializable.
    import json
    json.dumps(result.model_dump())
