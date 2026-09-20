# Resume Optimizer — a Claude Skill

A production-ready [Claude Skill](https://docs.claude.com/en/docs/build-with-claude/skills)
that reviews, rewrites, scores, and ATS-optimizes resumes — without
fabricating metrics, employers, or dates.

Paste a resume into Claude with the skill installed. Get back a rewritten
resume plus a structured report. That's it.

**License:** MIT · **Status:** v0.1.0 · **Hosts:** Claude Code, Claude
Desktop, claude.ai · **Optional:** local MCP server for PDF parsing

---

## What it does

Activates automatically on phrases like "review my resume", "ATS optimize
this", "tailor my CV for an AI role". Runs a 10-step workflow:

1. Extract structure
2. Analyze formatting
3. Analyze ATS compatibility
4. Score every section (0–5 with anchored rubric)
5. Detect weaknesses
6. Rewrite bullets (X-Y-Z, CAR, STAR formulas)
7. Improve grammar
8. Suggest measurable achievements **without inventing them**
9. Optimize for the inferred (or stated) target role
10. Produce a polished final resume **and** a structured report

Always returns two artifacts: the rewritten resume and a fixed-shape
report (scores, ATS findings, bullet rewrites, gap analysis, questions
for you). See [`resources/report-template.md`](./resources/report-template.md)
for the exact contract.

---

## Why this exists

Most resume-rewriting prompts hallucinate metrics. They turn "improved
performance" into "improved performance by 47%" without asking you. That
metric then sits on your resume waiting to fail a reference check.

This skill **refuses to fabricate**. Where the original resume lacks a
metric, the rewrite either:

- Stays qualitative, or
- Inserts a `[ADD IF TRUE: X%]` placeholder and asks you in the report.

Anti-fabrication is the single most load-bearing rule. See
[`resources/rewrite-rules.md`](./resources/rewrite-rules.md) §1.

---

## Install

### Claude Code

```bash
git clone https://github.com/sumukhmg/resume-optimizer-claude-skill
cd resume-optimizer-claude-skill

# macOS / Linux
mkdir -p ~/.claude/skills/resume-optimizer
cp -r skill/SKILL.md resources/ ~/.claude/skills/resume-optimizer/

# Windows (PowerShell)
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills\resume-optimizer"
Copy-Item -Recurse "skill/SKILL.md","resources" "$env:USERPROFILE\.claude\skills\resume-optimizer\"
```

Then open a Claude Code session and paste your resume.

### Claude Desktop / claude.ai

Upload `skill/SKILL.md` and the `resources/` directory into a Skill (or
Project knowledge file). The skill activates on the documented triggers.

### Inline (no install)

Paste the contents of [`skill/SKILL.md`](./skill/SKILL.md) into a fresh
Claude chat, prefaced with "Use the following skill for the rest of this
conversation." Then paste your resume.

Full install guide, including the optional MCP server for PDF parsing,
is in [`docs/installation.md`](./docs/installation.md).

---

## Quick demo

```
You: Improve my resume.
     [paste resume text]

Claude: [final rewritten resume]
        ---
        # Resume Review — Software Engineer (inferred)

        ## 1. Scores
        | Section          | Score | Reason                              |
        | ---------------- | ----- | ----------------------------------- |
        | Header / contact | 4/5   | Strong but contains photo (cut).    |
        | Experience       | 2/5   | "Responsible for…" in 4 bullets.    |
        | Skills           | 3/5   | Flat list; needs grouping.          |
        | ...

        ## 5. Bullet rewrites
        ### Example Corp — Software Engineer
        **Before:** Responsible for building features for the platform.
        **After:**  Shipped 4 React + TypeScript components for the
                    customer dashboard, used by [ADD IF TRUE: N teams].
        **Why:**    Removed banned opener; added scope; placeholder for
                    metric the user must confirm.

        ## 7. Questions for the user
        1. How many teams use the components you shipped?
        2. Did the latency optimization run in production or just dev?
        ...
```

See [`examples/`](./examples/) for seven realistic before/after pairs
across personas from student to senior engineer.

---

## Repository tour

| Path | What's in it |
| ---- | ----- |
| [`skill/SKILL.md`](./skill/SKILL.md) | The skill itself — activation, constraints, workflow. |
| [`resources/`](./resources/) | Rules, rubric, templates, keyword vocabularies. Loaded by the skill on demand. |
| [`examples/`](./examples/) | 7 worked before/after pairs with rule citations. |
| [`docs/`](./docs/) | Install, usage, architecture, contributor recipes. |
| [`mcp-server/`](./mcp-server/) | Optional Python MCP server (PDF parsing). |
| [`tests/`](./tests/) | Prompt-eval harness + YAML cases. |
| [`.github/`](./.github/) | Issue templates, PR template, CI. |

Read [`docs/architecture.md`](./docs/architecture.md) for why it's
split this way.

---

## Optional: MCP server

If you want to feed PDF resumes (instead of pasting text), install the
optional MCP server:

```bash
cd mcp-server
pip install -e .
```

Register `resume-optimizer-mcp` in your Claude host's MCP config (see
[`docs/mcp-server.md`](./docs/mcp-server.md)). Current tools:

| Tool | Status |
| ---- | ------ |
| `parse_pdf` | shipped |
| `parse_docx` | planned |
| `analyze_job_description` | planned |
| `match_resume_to_job` | planned |
| `gap_analysis` | planned |

Roadmap and contribution guide:
[`docs/mcp-server.md`](./docs/mcp-server.md).

---

## Domains tailored

The skill picks one (or two) of these keyword files automatically based
on the resume's strongest signal:

- Software Engineering (generic) · [`resources/keywords/software-engineering.md`](./resources/keywords/software-engineering.md)
- Backend / Distributed systems · [`resources/keywords/backend.md`](./resources/keywords/backend.md)
- Frontend / UI · [`resources/keywords/frontend.md`](./resources/keywords/frontend.md)
- AI / ML · [`resources/keywords/ai-ml.md`](./resources/keywords/ai-ml.md)
- DevOps / SRE / Platform · [`resources/keywords/devops.md`](./resources/keywords/devops.md)
- Cloud (AWS / Azure / GCP) · [`resources/keywords/cloud.md`](./resources/keywords/cloud.md)
- Data Science / Analytics · [`resources/keywords/data-science.md`](./resources/keywords/data-science.md)
- Research / Academic CV · [`resources/keywords/research.md`](./resources/keywords/research.md)

Adding keywords to your domain is the highest-leverage way to
contribute. See [`docs/adding-keywords.md`](./docs/adding-keywords.md).

---

## Contributing

PRs welcome. The fastest paths:

- **New keywords** → [`docs/adding-keywords.md`](./docs/adding-keywords.md)
- **New examples** → [`docs/adding-examples.md`](./docs/adding-examples.md)
- **New MCP tool** → [`mcp-server/README.md`](./mcp-server/README.md)
- **Anything else** → [`CONTRIBUTING.md`](./CONTRIBUTING.md)

For bug reports, especially fabrication bugs, see
[`SECURITY.md`](./SECURITY.md).

---

## License

[MIT](./LICENSE). Use it, fork it, ship it.

---

## Acknowledgements

Built for Anthropic's [Claude Skills](https://docs.claude.com/en/docs/build-with-claude/skills)
and [Model Context Protocol](https://modelcontextprotocol.io) primitives.
The rubric, recruiter checklist, and bullet formulas draw on widely-used
hiring conventions (X-Y-Z popularized by Google's career coaching;
CAR/STAR are standard interview frameworks).
