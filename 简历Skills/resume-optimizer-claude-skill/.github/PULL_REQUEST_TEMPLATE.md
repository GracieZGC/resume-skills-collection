# Pull Request

## What does this change?

<!-- One or two sentences. What changed and why. -->

## Type of change

<!-- Tick all that apply. -->

- [ ] Skill body (`skill/SKILL.md`)
- [ ] Rules / rubric / templates (`resources/`)
- [ ] Keyword vocabularies (`resources/keywords/`)
- [ ] Examples (`examples/`)
- [ ] MCP server (`mcp-server/`)
- [ ] Documentation (`docs/`, `README.md`)
- [ ] Tests (`tests/`)
- [ ] CI / release tooling

## Checklist

- [ ] I have read [`CONTRIBUTING.md`](../CONTRIBUTING.md).
- [ ] My changes do not duplicate content across `SKILL.md` and `resources/`.
- [ ] If I touched rewrite rules, scoring, or the workflow, I considered whether
      the change is a **minor** (additive / clarifying) or **major** (breaking
      the workflow / report contract) version bump per [`docs/architecture.md`](../docs/architecture.md).
- [ ] If I added or changed an example, the rewrite follows
      [`resources/rewrite-rules.md`](../resources/rewrite-rules.md) — no
      invented metrics, employers, or dates.
- [ ] If I added a keyword, I checked the criteria in [`docs/adding-keywords.md`](../docs/adding-keywords.md).
- [ ] If I added an MCP tool, I added a matching test under `mcp-server/tests/`.
- [ ] If I changed the report structure, I updated [`tests/cases/report-structure.yaml`](../tests/cases/report-structure.yaml) and bumped the major version in `CHANGELOG.md`.

## Related issues

<!-- e.g. Closes #123 -->
