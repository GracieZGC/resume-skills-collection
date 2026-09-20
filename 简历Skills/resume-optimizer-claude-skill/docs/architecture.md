# Architecture

The skill has three layers:

1. **Skill body** (`skill/SKILL.md`) — the entry point Claude loads.
   Intentionally short. Defines activation triggers, hard constraints,
   the workflow outline, the output contract, and resource-routing.
2. **Resources** (`resources/`) — the rules, rubrics, templates, and
   keyword vocabularies. Loaded on demand by the skill, file by file,
   per workflow step.
3. **MCP server** (`mcp-server/`, optional) — out-of-band capabilities
   like PDF parsing. The skill interface does not change when MCP is
   present; the host decides whether to call MCP tools before sending
   text to the skill.

```
                ┌──────────────────────────┐
   user ───▶    │  Claude Code / Desktop   │
                │  loads SKILL.md          │
                └──────────┬───────────────┘
                           │ workflow step N triggers a load
                           ▼
                ┌──────────────────────────┐
                │  resources/<file>.md     │
                │  rules, rubric, keywords │
                └──────────────────────────┘
                           ▲
                           │ updated by contributors
                ┌──────────────────────────┐
                │  examples/<persona>/...  │
                │  (read by contributors,  │
                │   not by the skill)      │
                └──────────────────────────┘

                  optional, host-side
                ┌──────────────────────────┐
   PDF/DOCX ───▶│  mcp-server (Python)     │
   files        │  parse_pdf, ...          │
                └──────────┬───────────────┘
                           │ extracted text
                           ▼
                  Claude (skill runs as above)
```

---

## Why the skill is short

Skills are loaded into every conversation that activates them. A long
skill burns context the user could spend on their resume and report.
Three principles keep `SKILL.md` short:

- **No duplication.** A rule that lives in `resources/rewrite-rules.md`
  does not also live in `SKILL.md`. The skill **references** it.
- **No examples in the skill body.** Examples live in `examples/`, for
  contributors to read. Claude does not need them at runtime.
- **No restatement of resources.** The skill says "load
  `resources/workflow.md` and follow it step by step", not "step 1:
  extract structure; step 2: …". The resource is the source of truth.

---

## Why resources are split per concern

A monolithic `rules.md` would force every conversation to load the
whole file, even when the workflow step needs only one chapter. Splitting
by concern lets the skill load only what each step requires (see the
load table in [`../resources/README.md`](../resources/README.md)).

It also gives contributors a clear contract: a PR that touches `ATS
keyword vocabulary` is purely a `keywords/<file>.md` change; it never
touches the skill or the rubric. Reviewing those PRs is fast.

---

## Why MCP is a separate scaffold

PDF parsing is a real capability, but it has a different lifecycle from
the skill:

- It runs on the user's machine (or a host with FS access), not in the
  Claude chat.
- It requires Python packages (`pypdf`, `pdfplumber`).
- It evolves at a different rate than the prompting work.

Keeping MCP as a separate package (`mcp-server/`) means:

- Users who only want the skill don't need to install Python.
- Contributors who want to add capabilities (DOCX, JD scrape, gap
  analysis) can do so without touching prompts.
- The skill's interface stays stable — adding a new MCP tool doesn't
  require a skill release.

See [`mcp-server.md`](./mcp-server.md) for the capability roadmap.

---

## Stability contract

Across minor versions:

- The 10-step **workflow** in `resources/workflow.md` is stable. Adding
  a step is a major version bump.
- The **report structure** in `resources/report-template.md` is stable.
  Downstream tools depend on the section order.
- The **resource filenames** are stable. Renaming a resource file is
  also a major version bump.
- The **skill name** (`resume-optimizer`) is stable.

What can change in a minor version:

- Wording of rules, as long as semantics are preserved.
- New keywords added to existing domain files.
- New examples.
- New MCP tools (additive only).

See [`../CHANGELOG.md`](../CHANGELOG.md) for the version history.

---

## Where to start reading the code

For contributors, the natural reading order is:

1. [`../skill/SKILL.md`](../skill/SKILL.md) — the entry point.
2. [`../resources/workflow.md`](../resources/workflow.md) — the
   pipeline the skill executes.
3. [`../resources/rewrite-rules.md`](../resources/rewrite-rules.md) —
   the invariants every step honors.
4. [`../resources/report-template.md`](../resources/report-template.md) —
   the output contract.
5. [`../examples/`](../examples/) — how the rules manifest on real
   resumes.

After that, the keyword files and rubric round out the picture.
