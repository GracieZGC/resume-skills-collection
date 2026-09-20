"""Pydantic schemas shared across MCP tools.

Keep types narrow and documented — they appear in the tool's JSON schema
that the host sends to Claude. Vague types make the model guess.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class ParsePdfInput(BaseModel):
    """Input for the parse_pdf tool."""

    path: str = Field(
        ...,
        description="Absolute or working-directory-relative path to a PDF file.",
    )
    max_pages: int = Field(
        default=10,
        ge=1,
        le=50,
        description="Maximum pages to read. Resumes are 1-3 pages; CVs are longer.",
    )


class ParsePdfOutput(BaseModel):
    """Output for the parse_pdf tool."""

    text: str = Field(..., description="Concatenated text content from the PDF.")
    pages_read: int = Field(..., description="Number of pages actually read.")
    warnings: list[str] = Field(
        default_factory=list,
        description=(
            "Non-fatal warnings the caller should surface to the user. "
            "Examples: 'PDF appears to contain images of text (likely scanned).'"
        ),
    )
