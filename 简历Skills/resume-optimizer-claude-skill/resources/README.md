# Resources

This directory holds the reference material the Resume Optimizer skill
loads on demand. The skill itself (`skill/SKILL.md`) is intentionally
short — these files are where the rules, rubrics, and vocabularies live.

Two reasons to keep things split:

1. **Context budget.** The skill body is loaded into every conversation
   that activates it. Long skills eat context. Short skill + targeted
   resource loads keeps the surface lean.
2. **Contribution.** Adding new keywords, sharpening the rubric, or
   tuning rewrite rules is a one-file change. Contributors don't need to
   touch the skill itself.

---

## When the skill loads each file

| Workflow step | File | Notes |
|---|---|---|
| Always | [`rewrite-rules.md`](./rewrite-rules.md) | Anti-fabrication and rewrite invariants. Load every run. |
| Always | [`workflow.md`](./workflow.md) | The 10 steps the skill executes. |
| Step 10 | [`report-template.md`](./report-template.md) | Fixed output shape. |
| Step 2 | [`ats-rules.md`](./ats-rules.md) | Formatting and ATS findings. |
| Step 3 | [`ats-rules.md`](./ats-rules.md) | Used again for ATS-specific risk ranking. |
| Step 4 | [`scoring-rubric.md`](./scoring-rubric.md) | Section-by-section scoring. |
| Step 5 | [`recruiter-checklist.md`](./recruiter-checklist.md) | 6-second-scan and red flags. |
| Step 6 | [`bullet-formulas.md`](./bullet-formulas.md) | X-Y-Z, CAR, STAR. |
| Step 6 | [`action-verbs.md`](./action-verbs.md) | Categorized strong openers. |
| Step 7 | [`grammar-style.md`](./grammar-style.md) | Tense, voice, parallelism, numerals. |
| Step 9 | [`keywords/<domain>.md`](./keywords/) | One file, picked by inferred or stated target role. |

The skill is allowed (and expected) to load multiple files in the same
step — e.g., step 6 reads both `bullet-formulas.md` and `action-verbs.md`.

---

## Domain keyword files

Picked at workflow step 9 based on the resume's strongest signal or the
stated target role:

| File | Roles |
|---|---|
| [`keywords/software-engineering.md`](./keywords/software-engineering.md) | General SWE, no further specialization given. |
| [`keywords/backend.md`](./keywords/backend.md) | Backend, distributed systems, platform-eng services. |
| [`keywords/frontend.md`](./keywords/frontend.md) | Frontend, UI, full-stack (frontend-heavy). |
| [`keywords/ai-ml.md`](./keywords/ai-ml.md) | AI engineer, ML engineer, applied scientist. |
| [`keywords/devops.md`](./keywords/devops.md) | DevOps, SRE, platform engineering. |
| [`keywords/cloud.md`](./keywords/cloud.md) | Cloud engineer / architect, cloud-specialist. |
| [`keywords/data-science.md`](./keywords/data-science.md) | Data scientist, data analyst, data engineer, analytics. |
| [`keywords/research.md`](./keywords/research.md) | Research engineer, research scientist, PhD candidate, academic CV. |

It is correct (and common) to combine two domain files when the role
spans both — e.g., a research engineer working on LLMs reads both
`research.md` and `ai-ml.md`.

---

## What this directory does **not** contain

- The skill body itself → [`../skill/SKILL.md`](../skill/SKILL.md).
- Worked examples → [`../examples/`](../examples/).
- Architecture / contributor docs → [`../docs/`](../docs/).

If you find yourself duplicating a rule, rubric, or vocabulary between
the skill and a resource, the duplicate belongs in the resource. See
[../CONTRIBUTING.md](../CONTRIBUTING.md).
