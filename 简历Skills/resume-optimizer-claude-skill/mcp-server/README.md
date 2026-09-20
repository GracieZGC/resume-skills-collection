# resume-optimizer-mcp

Optional MCP server for the [Resume Optimizer Claude Skill](../).

Provides out-of-band capabilities the skill itself cannot — currently
PDF parsing. The skill works without this server; install it only if
you want to feed PDF files (instead of pasted text) into the workflow.

See [`../docs/mcp-server.md`](../docs/mcp-server.md) for the rationale,
roadmap, and architecture.

---

## Install

Requires Python 3.11+.

```bash
pip install -e .
# or with uv:
uv pip install -e .
```

## Register with the Claude host

Claude Code (`~/.claude/mcp.json` or your host's MCP config):

```json
{
  "mcpServers": {
    "resume-optimizer": {
      "command": "resume-optimizer-mcp",
      "args": []
    }
  }
}
```

Claude Desktop: use the host's MCP UI to add a server pointing at the
`resume-optimizer-mcp` command.

## Tools

| Tool | Status | Description |
|---|---|---|
| `parse_pdf` | shipped | Extract text from a PDF resume. Returns plain text + warnings. |
| `parse_docx` | planned | Same, for `.docx`. |
| `analyze_job_description` | planned | Extract keywords / level / years from a JD. |
| `match_resume_to_job` | planned | Resume ↔ JD keyword scoring. |
| `extract_ats_keywords` | planned | What an ATS would see. |
| `gap_analysis` | planned | Resume vs target role gap report. |
| `compare_resumes` | planned | Diff two resume versions. |

See the roadmap in [`../docs/mcp-server.md`](../docs/mcp-server.md).

## Adding a tool

1. Add an input/output schema pair to `src/resume_optimizer_mcp/schemas.py`.
2. Add a module to `src/resume_optimizer_mcp/tools/<name>.py` with a
   pure function `name(input: NameInput) -> NameOutput`.
3. Export it from `src/resume_optimizer_mcp/tools/__init__.py`.
4. Register it in `TOOLS` in `src/resume_optimizer_mcp/server.py`.
5. Add a test in `tests/test_<name>.py`.

The reference implementation is `tools/parse_pdf.py`. Match its shape.

## Tests

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT. See [`../LICENSE`](../LICENSE).
