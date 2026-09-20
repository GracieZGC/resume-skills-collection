# Contributing

Thanks for considering a contribution. The Resume Optimizer is a
prompt-engineering project as much as a software project, which means
contributions look a little different from a typical OSS repo: you'll
mostly edit markdown, and the highest-leverage changes are often the
smallest.

This doc covers the quick paths for the most common contributions and
the longer paths for changes that touch the core skill.

---

## Quick paths

### Add keywords to a domain file

See [`docs/adding-keywords.md`](./docs/adding-keywords.md). Open the
"New keywords" issue if you want to discuss first, or skip straight to
the PR.

### Add or improve an example

See [`docs/adding-examples.md`](./docs/adding-examples.md). Each new
persona is ~3 files (before/after/notes) and one row in
`examples/README.md`.

### Fix a typo, link, or formatting issue

Open a PR. No issue needed.

### Add an MCP tool

See the "Adding a tool" section of
[`mcp-server/README.md`](./mcp-server/README.md) and the capability
roadmap in [`docs/mcp-server.md`](./docs/mcp-server.md).

---

## Longer paths

### Change the rewrite rules, scoring rubric, or workflow

These are the load-bearing files for the whole project. Open an issue
first describing the rule you want to change and why. A change to the
**workflow** (e.g., adding or removing a step), the **report
structure**, or the **anti-fabrication rules** is a major version bump
per [`docs/architecture.md`](./docs/architecture.md) and may need
broader discussion.

### Change the skill body (`SKILL.md`)

`SKILL.md` is intentionally short. Most additions belong in
`resources/`. Before adding content to `SKILL.md`, ask: could this be
a resource the skill loads on demand? Almost always, yes. The skill
body should not duplicate any rule or vocabulary that lives in a
resource file.

If you do need to change `SKILL.md`:

- Preserve the frontmatter (`name`, `description`, `license`).
- Preserve the activation-trigger list — adding triggers is fine,
  removing them is a breaking change.
- Preserve the output contract.

---

## Development setup

For text-only contributions (markdown), no setup is needed. For the
MCP server:

```bash
cd mcp-server
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
```

For the prompt-eval suite:

```bash
pip install anthropic pyyaml
export ANTHROPIC_API_KEY=sk-...
python tests/eval_harness.py
```

---

## Style

- Two-space markdown indent (see `.editorconfig`).
- Plain markdown only. No HTML, no embedded images.
- Use `[`...`](./relative/path)` links between repo files so they survive
  on GitHub and in offline viewers.
- Filenames are `kebab-case.md`.
- When citing a rule, link the file and the section: `rewrite-rules.md
  §1`. The skill and tests rely on these references staying current.

---

## Review

Most PRs get a first review within a few business days. Faster paths:

- **Keyword additions** — usually 1 day.
- **Typos / linting** — same day.
- **New examples** — 2–5 days (we read examples carefully because they
  teach by shape).
- **Rule changes** — depends on the rule, but discuss in an issue first.

Reviews focus on:

1. Does the change follow the rule files?
2. Does the change avoid duplication?
3. Does the change preserve the existing stability contracts?
4. Is the change easy to maintain (no extra moving parts)?

---

## Reporting issues

- For bugs, use the **Bug report** issue template. If the skill
  fabricated a metric, employer, or date, please add the `fabrication`
  label — those are release-blockers.
- For ideas, use the **Feature request** template. Describe the user
  scenario before prescribing a solution.
- For keyword suggestions, use the dedicated **New keywords** template.

---

## Code of Conduct

This project follows the
[Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
Be kind. Disagreements about technical decisions are welcome;
disagreements about whether someone deserves respect are not. See
[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

---

## License

By contributing, you agree your contributions are licensed under the
project's [MIT License](./LICENSE).
