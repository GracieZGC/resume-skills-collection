"""Stdio MCP server entry point.

Register new tools in TOOLS below. Each tool needs:
- a Pydantic input model (defines the JSON schema the host sends to Claude)
- a function that returns a Pydantic output model
- a one-line description that appears to Claude in the tool list

The server uses the official `mcp` Python SDK (https://github.com/modelcontextprotocol).
"""

from __future__ import annotations

import asyncio
import json
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from .schemas import ParsePdfInput
from .tools import parse_pdf

# Tool registry. To add a tool: add the entry here, plus a module under tools/.
TOOLS: dict[str, dict[str, Any]] = {
    "parse_pdf": {
        "description": "Extract text from a PDF resume on disk. Returns plain text the skill can review.",
        "input_model": ParsePdfInput,
        "handler": parse_pdf,
    },
}


def _tool_definitions() -> list[Tool]:
    """Build the MCP Tool list from the registry."""
    return [
        Tool(
            name=name,
            description=meta["description"],
            inputSchema=meta["input_model"].model_json_schema(),
        )
        for name, meta in TOOLS.items()
    ]


async def _run() -> None:
    server: Server = Server("resume-optimizer-mcp")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return _tool_definitions()

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
        if name not in TOOLS:
            raise ValueError(f"Unknown tool: {name}")
        meta = TOOLS[name]
        input_obj = meta["input_model"].model_validate(arguments)
        result = meta["handler"](input_obj)
        # Result is a Pydantic model → JSON-encode for the host.
        return [TextContent(type="text", text=json.dumps(result.model_dump(), indent=2))]

    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main() -> None:
    """Console entry point declared in pyproject.toml [project.scripts]."""
    asyncio.run(_run())


if __name__ == "__main__":
    main()
