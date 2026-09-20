# Examples

Seven realistic before/after pairs, one per persona, illustrating how the
skill applies its rules to common resume problems. Each directory has:

- `before.md` — a representative weak (or under-optimized) version
- `after.md` — the rewrite the skill would produce
- `notes.md` — what changed and why, citing the rule files

The "before" examples are intentionally flawed in the ways resumes
actually fail — vague bullets, missing metrics, weak verbs, ATS pitfalls,
seniority drift, padded skills. They are **not** strawmen.

The "after" examples follow [`../resources/rewrite-rules.md`](../resources/rewrite-rules.md)
strictly. **Where the "before" had no metric**, the "after" either omits
the metric (preserving honesty) or uses a `[ADD IF TRUE: …]` placeholder.
We never invent numbers, even in examples.

---

## Personas

| Persona | Directory | Strongest signal |
|---|---|---|
| Student (no full-time experience) | [student/](./student/) | Coursework + projects + one internship. |
| New graduate | [new-grad/](./new-grad/) | Recent degree + internships + projects. |
| Software engineer (mid-level) | [software-engineer/](./software-engineer/) | 3–5 yrs SWE. |
| Backend engineer | [backend-engineer/](./backend-engineer/) | Distributed systems / services. |
| AI engineer | [ai-engineer/](./ai-engineer/) | Applied ML / LLM productionization. |
| Research engineer | [research-engineer/](./research-engineer/) | Industrial research / publications. |
| Senior engineer | [senior-engineer/](./senior-engineer/) | 8+ yrs, scope and leadership. |

---

## How to read these

For each persona:

1. Read `before.md` and **find the issues yourself** before scrolling.
2. Read `after.md`.
3. Read `notes.md` to check whether your diagnosis matches the skill's.

The examples deliberately do **not** include real names, employers, or
metrics. Anything in `[brackets]` is an illustrative placeholder. None
of these are real people.

---

## What examples do **not** cover

- Country-specific formatting (German "Lebenslauf", Japanese "rirekisho",
  US-style federal resumes). These need their own conventions; the
  skill's rules are international where possible but the examples lean
  US/EU standard.
- Heavily designed visual resumes (Canva-style, two-column infographic).
  See [`../resources/ats-rules.md`](../resources/ats-rules.md) §1 for
  why those usually need to be reformatted before rewriting.
- Cover letters. Different artifact, different rules. Out of scope for
  this skill in its current form.
