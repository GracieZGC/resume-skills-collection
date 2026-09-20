# MCP Server

The repository ships with an **optional** MCP (Model Context Protocol)
server, `resume-optimizer-mcp`, that adds out-of-band capabilities the
skill itself cannot provide — like parsing a PDF resume on disk.

The skill works fine without it. If you only paste resume text into
chat, you do not need the MCP server.

---

## Why MCP at all?

The Claude Skill is a **prompt** — it runs inside the model. There are
things a prompt cannot do:

- Read a binary file (PDF, DOCX, RTF).
- Hit an external URL on the user's network.
- Persist or cache anything between conversations.

MCP solves that. The server runs locally (or wherever the host can
reach), exposes typed tools, and the host can call them to enrich the
context the skill operates on.

Crucially: the **skill's interface does not change** when MCP is
present. The skill takes resume text and produces a rewrite + report.
MCP just provides a better way to get the resume text in.

---

## What's in the scaffold today

`mcp-server/` contains a working stdio MCP server with **one** reference
tool, `parse_pdf`, to demonstrate the architecture. It is intentionally
scaffold-shaped, not exhaustive — see the roadmap below for what
additional tools are planned.

```
mcp-server/
├── pyproject.toml
├── README.md
├── src/resume_optimizer_mcp/
│   ├── __init__.py
│   ├── server.py        # stdio entry point + tool registry
│   ├── schemas.py       # shared Pydantic models
│   └── tools/
│       ├── __init__.py
│       └── parse_pdf.py # one working tool
└── tests/
    └── test_parse_pdf.py
```

Adding a new tool is a single-file change in `tools/` plus a single
line in `server.py`'s registry. See `tools/parse_pdf.py` for the
shape.

---

## Capability roadmap

In priority order. Each is a single tool, additive (no breaking changes
to the skill or to other tools):

1. **`parse_pdf`** — extract resume text from a PDF. **Shipped.**
2. **`parse_docx`** — same, for `.docx` files. Uses `python-docx`.
3. **`analyze_job_description`** — take a JD (URL or text), extract the
   top ~15 keywords and required years/level. Feeds workflow step 9.
4. **`match_resume_to_job`** — score the resume's keyword overlap with
   a parsed JD. Returns the gap analysis the report's §6 expects.
5. **`extract_ats_keywords`** — given a resume, surface the keywords
   currently visible to an ATS (after parsing as an ATS would).
   Useful for "what does the recruiter actually see?" diagnostics.
6. **`gap_analysis`** — given a resume + target role, return the
   keyword gaps grouped by "supported by experience" vs "genuine
   gap" (per rewrite-rules.md §7).
7. **`compare_resumes`** — diff two resumes side by side. Useful when
   a candidate iterates and wants to see what changed across versions.

Each of these is welcome as a contribution. See
[`../CONTRIBUTING.md`](../CONTRIBUTING.md) for the contribution flow.

---

## Installing the MCP server

Requires Python 3.11+.

```bash
cd mcp-server
pip install -e .
# Or with uv:
uv pip install -e .
```

To register with Claude Code, add an entry to your MCP config
(`~/.claude/mcp.json` or the host's equivalent):

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

To register with Claude Desktop, use the host's MCP UI to add a server
pointing at the `resume-optimizer-mcp` command.

---

## Running tests

```bash
cd mcp-server
pip install -e ".[dev]"
pytest
```

The test for `parse_pdf` uses a small fixture PDF stored under
`tests/fixtures/`. New tools should add a fixture-based test in the
same shape.

---

## Stability contract

- Tool **names** are stable across minor versions.
- Tool **schemas** can grow (additive fields only) within minor
  versions. Removing or renaming a field is a major version bump.
- A **new tool** is always additive — it does not change the skill or
  any other tool.

See [`../CHANGELOG.md`](../CHANGELOG.md) for the version history.
