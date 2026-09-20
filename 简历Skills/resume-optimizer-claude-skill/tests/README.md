# Tests

Resume optimization is a **prompt-eval** problem, not a unit-test
problem. There is no single deterministic "correct" rewrite of a
resume. The tests here therefore verify **structural and behavioral
properties** that the skill must hold across runs:

- Activation triggers fire on the documented phrases.
- Output contains both artifacts (rewrite + report).
- The report's section structure matches `report-template.md`.
- No fabrication: the skill does not invent metrics, employers, or
  dates that aren't in the input.
- ATS landmines in the input get flagged in the output.

If a future contribution wants stricter property checks (e.g.,
golden-output diffs across model versions), add them — but the four
files in `cases/` are the load-bearing set.

---

## Layout

```
tests/
├── README.md           # this file
├── eval_harness.py     # the runner: load skill, call Claude, assert
├── cases/
│   ├── activation.yaml      # trigger phrases activate the skill
│   ├── no-fabrication.yaml  # skill doesn't invent metrics/companies/dates
│   ├── report-structure.yaml # output has all 8 report sections
│   └── ats-flags.yaml       # skill detects tables, icons, columns
└── fixtures/
    └── sample-resume.md     # one realistic resume the cases reuse
```

Each YAML case has the shape:

```yaml
name: A short identifier
description: One sentence about what this case is checking.
prompt: |
  The user message to send.
inputs:
  resume: fixtures/sample-resume.md   # optional; pasted into the prompt
assertions:
  - contains: "regex or literal string"
  - not_contains: "regex or literal string"
  - section_present: "## 1. Scores"
  - section_present: "## 5. Bullet rewrites"
```

Assertion types implemented in `eval_harness.py`:

- `contains: <str>` — substring or regex must be present.
- `not_contains: <str>` — substring or regex must be absent.
- `section_present: <heading>` — heading line must appear verbatim.

The runner is intentionally simple. If you need richer assertions,
extend it — but keep cases declarative.

---

## Running the suite

Requires an Anthropic API key.

```bash
export ANTHROPIC_API_KEY=sk-...     # or set in your shell profile
cd tests
pip install anthropic pyyaml
python eval_harness.py
```

Per case the runner:

1. Loads the skill body (`../skill/SKILL.md`).
2. Constructs a single-turn prompt: skill system message + user message.
3. Sends to Claude via the Anthropic SDK.
4. Evaluates the assertions against the response.

Exit code is non-zero if any case fails.

If `ANTHROPIC_API_KEY` is unset, the runner exits 0 with a "skipped"
message — this lets CI run lint without API access (see
`.github/workflows/test.yml`).

---

## Adding a case

1. Create `cases/<name>.yaml` following the schema above.
2. Make sure the assertions trace to a rule. Cases that don't trace to
   a rule become flaky over time.
3. Run the suite locally once with `python eval_harness.py` to check
   the case passes on the current model.
4. Open a PR.

---

## What these tests do **not** cover

- **Quality** of rewrites. We don't have a way to assert "this bullet
  is better than that bullet" automatically. Quality regressions are
  caught by review of the `examples/` directory, not the test suite.
- **Cost / latency.** Out of scope.
- **MCP server tools.** Those have their own pytest suite under
  `../mcp-server/tests/`.
