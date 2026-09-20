# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

For what counts as a major vs. minor change, see the "Stability contract"
section of [`docs/architecture.md`](./docs/architecture.md).

## [Unreleased]

## [0.1.0] — 2026-06-30

Initial public release.

### Added

- Claude Skill (`skill/SKILL.md`) with activation triggers, hard
  constraints, the 10-step workflow, the output contract, and domain
  routing.
- Reference resources under `resources/`:
  - `rewrite-rules.md` — anti-fabrication and rewrite invariants.
  - `workflow.md` — the 10-step pipeline.
  - `scoring-rubric.md` — section-by-section 0–5 scoring.
  - `recruiter-checklist.md` — 6-second-scan and red flags.
  - `ats-rules.md` — formatting and ATS parsing rules.
  - `bullet-formulas.md` — X-Y-Z, CAR, STAR.
  - `action-verbs.md` — categorized strong verbs, banned openers.
  - `grammar-style.md` — tense, voice, parallelism, numerals, buzzwords.
  - `report-template.md` — fixed 8-section report structure.
- Domain keyword files for software engineering, backend, frontend,
  AI/ML, DevOps, cloud, data science, and research.
- Seven worked examples (`examples/`): student, new graduate, software
  engineer, backend engineer, AI engineer, research engineer, senior
  engineer. Each has `before.md`, `after.md`, `notes.md`.
- Documentation (`docs/`): installation, usage, architecture, contributor
  recipes for keywords and examples, MCP overview.
- Optional MCP server scaffold (`mcp-server/`) with a working `parse_pdf`
  reference tool and pytest suite.
- Prompt-eval harness (`tests/`) with 4 YAML cases: activation,
  no-fabrication, report-structure, ats-flags.
- GitHub: issue templates (bug, feature, keywords), PR template, CI
  workflows (lint, test, release), release-notes template.
- Repo governance: MIT License, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY.

[Unreleased]: https://github.com/Sumukhmg/resume-optimizer-claude-skill/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Sumukhmg/resume-optimizer-claude-skill/releases/tag/v0.1.0
