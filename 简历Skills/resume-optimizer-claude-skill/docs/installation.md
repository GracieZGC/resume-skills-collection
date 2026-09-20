# Installation

The Resume Optimizer is a **Claude Skill** — a single `SKILL.md` plus
the supporting resources, examples, and (optional) MCP server in this
repository. There are three ways to install it depending on which Claude
host you use.

If you only want to try it once, **clone the repo and copy/paste**
`skill/SKILL.md` into a Claude chat alongside your resume. That works
without any installation at all.

---

## Option 1 — Claude Code (CLI)

The skill is invoked automatically when its activation triggers fire in
a Claude Code session.

```bash
# 1. Clone the repository.
git clone https://github.com/Sumukhmg/resume-optimizer-claude-skill
cd resume-optimizer-claude-skill

# 2. Install the skill into your Claude Code skills directory.
# On macOS/Linux:
mkdir -p ~/.claude/skills/resume-optimizer
cp -r skill/SKILL.md resources/ ~/.claude/skills/resume-optimizer/

# On Windows (PowerShell):
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills\resume-optimizer"
Copy-Item -Recurse "skill/SKILL.md","resources" "$env:USERPROFILE\.claude\skills\resume-optimizer\"
```

Then start a Claude Code session and paste a resume. The skill activates
on phrases like "review my resume", "ATS optimize this", etc. — see
[`usage.md`](./usage.md) for the full trigger list.

---

## Option 2 — Claude Desktop / claude.ai with Projects

Claude Desktop and claude.ai both support custom skills via the Skills
or Projects UI. The exact path is product-dependent; the **content** to
upload is the same.

1. Create a new Skill (or Project knowledge file).
2. Upload `skill/SKILL.md` and the entire `resources/` directory.
3. Save / activate.

The skill is now available in conversations within that Skill/Project
context.

---

## Option 3 — Inline (no installation)

For a one-shot use:

1. Open the latest [`SKILL.md`](../skill/SKILL.md) on GitHub.
2. Copy its contents.
3. Open a fresh Claude chat and send the SKILL.md text in your first
   message, prefaced with: "Use the following skill for the rest of this
   conversation."
4. Send your resume in the next message.

Limitations of the inline path:

- Resources are not auto-loaded. The skill will reference them by
  filename, but Claude can't read them. You can either paste the
  specific resource files you want it to use, or accept that some rules
  (rubric, keyword files) won't be applied with full depth.
- No MCP support. PDF/DOCX parsing requires the MCP server (Option 4).

---

## Option 4 — Optional MCP server

Adds PDF parsing (and, in the future, DOCX parsing, JD matching, and
others). The MCP server is **optional**; the skill works without it as
long as the user pastes resume text.

See [`mcp-server.md`](./mcp-server.md) for the install steps and
capability roadmap.

---

## Verifying installation

After installing on Claude Code or Desktop:

1. Open a fresh conversation.
2. Paste a short resume (or one of [`../examples/*/before.md`](../examples/)).
3. Say: "Review my resume."

If the skill is installed correctly, the response should produce two
artifacts (rewritten resume + report) and follow the structure in
[`../resources/report-template.md`](../resources/report-template.md). If
it doesn't, see the troubleshooting section in [`usage.md`](./usage.md).
