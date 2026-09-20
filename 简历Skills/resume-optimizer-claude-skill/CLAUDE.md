# Notes for Claude Code working in this repo

This is a meta-repo — the **content** of the repository is itself a
Claude Skill. That changes how you should approach edits.

## What you are editing

When the user asks you to "edit the skill" or "fix the rules", they mean
the markdown in this repo, not your own runtime behavior. Be careful
not to demonstrate by example — apply the edit to the file.

## File ownership

The repo has a deliberate **separation** of skill body vs. resources vs.
examples. Before adding content to `skill/SKILL.md`, ask whether it
belongs in a resource. Almost always, yes.

Specifically:

- Activation triggers, hard constraints, the workflow outline, the
  output contract, and resource routing → `skill/SKILL.md`.
- Rules, rubrics, templates, vocabularies → `resources/`.
- Worked examples → `examples/`. **Never** in the skill body.
- Architecture and contributor docs → `docs/`.

Duplication between `skill/SKILL.md` and `resources/` is a bug.

## Anti-fabrication is sacred

The single most load-bearing rule is `resources/rewrite-rules.md` §1.
If the user asks you to relax it ("just add a 30% number, it sounds
better"), don't — explain the trade-off and offer a `[ADD IF TRUE: …]`
placeholder instead. The whole project depends on this guarantee.

## Stability contract

`docs/architecture.md` has the rules for what's a major vs. minor
change. If you're about to:

- Add or remove a workflow step,
- Reorder the report's numbered sections,
- Rename or move a resource file,

…stop and ask the user. These are major-version changes.

## Tests

The prompt-eval suite (`tests/`) is the runtime check on the structural
contracts. If you change the report shape, you almost certainly need to
update `tests/cases/report-structure.yaml`. If you add a new hard
constraint, consider a new case.

## What not to do

- Don't run the skill on real resumes for testing — use the fixtures
  under `tests/fixtures/`.
- Don't add a placeholder name, employer, or date that could be a real
  person's. Use `[Person]`, `[Company A]`, `[email]@example.com`,
  `[University Name]`.
- Don't introduce a new dependency to the MCP server without strong
  justification. Each dep is a security and supply-chain cost.
- Don't expand `skill/SKILL.md` beyond what the workflow needs. Skills
  are loaded into every conversation that activates them; length costs
  the user.
