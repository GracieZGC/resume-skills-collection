# Security Policy

## Scope

This is a **prompt-engineering project** — a Claude Skill plus an optional
local MCP server. The threat surface is small but non-zero. This document
explains what is in scope, what is not, and how to report findings.

### In scope

- **The MCP server (`mcp-server/`).** Bugs that could read files outside
  the documented input path, leak environment variables, or crash the
  server with crafted PDF input.
- **The skill's anti-fabrication guarantee.** If a malicious or
  cleverly-shaped resume input causes the skill to fabricate metrics,
  employers, or dates that aren't in the input, we treat that as a
  release-blocker.
- **Supply-chain risks** in dependencies (`pypdf`, `mcp`, `pydantic`,
  test deps).
- **Dependency-pinning oversights** in workflows (`actions/*` versions).

### Out of scope

- The accuracy of resume *advice*. Resume content quality is opinion,
  not security.
- Claude model behavior outside this skill (use Anthropic's
  responsible-disclosure channels for model-level issues).
- The user's choice of resume content. The skill processes whatever it
  is given.
- DoS via huge inputs to the MCP server when run locally. The server is
  a single-user tool; rate-limiting is not in scope.

## Reporting

For **security bugs in the MCP server or workflows**, please open a
[GitHub security advisory](https://github.com/sumukhmg/resume-optimizer-claude-skill/security/advisories/new)
rather than a public issue. We will respond within 7 days.

For **fabrication bugs in the skill** (the skill invented a metric,
employer, or date), open a public issue with the `fabrication` label and
attach:

- The exact prompt you used.
- The resume input (redacted as needed).
- The skill's output (redacted as needed).
- The Claude model used.

We treat fabrication as the most serious class of bug in this project.

For **Code of Conduct issues**, see [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

## Disclosure

We will:

1. Acknowledge the report within 7 days.
2. Confirm or dispute the issue within 14 days.
3. Ship a fix (or a documented workaround) for in-scope security bugs
   before public disclosure, on a timeline proportional to severity.

We do not currently run a bug-bounty program.

## Privacy of resume content

The skill itself processes only what the user pastes into the chat. We
do not store, log, or upload resume content from this repository's code
paths. The host (Claude Code, Claude Desktop, claude.ai) handles
conversation storage per its own policies — see your Claude host's
privacy documentation.

The optional MCP server reads only the path passed to its tools. It
does not phone home and does not log content to disk beyond what the
host's MCP transport already does.
