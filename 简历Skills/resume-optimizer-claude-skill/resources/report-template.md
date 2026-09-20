# Report Template

The skill's final output is **always two artifacts**: the rewritten resume
and this report. Both are produced in step 10 of the workflow.

The report is plain markdown. Section order is fixed so users (and any
downstream MCP tools that may post-process the output) can rely on it.

---

```markdown
# Resume Review — <Candidate Name or Inferred Role>

**Target role (inferred or stated):** <Role>
**Domain keyword file used:** <e.g., resources/keywords/ai-ml.md>
**Overall signal:** <one-sentence summary the recruiter would use to forward this>

---

## 1. Scores

| Section | Score (0–5) | One-line reason |
|---|---:|---|
| Header / contact | X | … |
| Summary | X | … |
| Experience | X | … |
| Education | X | … |
| Skills | X | … |
| Projects | X | … |
| (Publications, etc.) | X | … |

**Overall:** X/5 — <one-line summary, includes any cross-cutting cap from
scoring-rubric.md>

## 2. Formatting findings

(From workflow step 2. Skip the heading if there are zero findings, but
say so: "No formatting findings.")

- …

## 3. ATS findings

(From workflow step 3. Rank each as High / Medium / Low per ats-rules.md.)

- **High** — …
- **Medium** — …
- **Low** — …

## 4. Section-level weaknesses

(From workflow step 5. Group by section.)

### Experience

- …

### Skills

- …

### (etc.)

## 5. Bullet rewrites

(From workflow step 6. Always show before/after side by side. Mark
[CONFIRM] and [ADD IF TRUE: …] placeholders inline.)

### <Company> — <Role>

**Before:**
> Responsible for backend services and worked with the team on improvements.

**After:**
> Owned 4 backend services (Python/FastAPI, ~1.2k RPS peak), [CONFIRM]
> reducing p99 latency by [ADD IF TRUE: X%] through async I/O and connection
> pooling.

**Why:** Replaced "Responsible for / Worked with" with `Owned`; added scope
(service count, language, traffic); placeholder metric flagged for user
confirmation rather than fabricated.

(repeat per bullet rewritten)

## 6. Gap analysis

(From workflow step 9. Compare the resume against the keyword file or
provided JD.)

**Keywords present in resume:** <list>
**Keywords missing but supported by the user's experience** (recommend
re-wording existing bullets to surface): <list>
**Keywords missing AND not supported** (genuine gap, do not fabricate):
<list>

## 7. Questions for the user

(From workflow step 8. Group every `[ADD IF TRUE]` and clarifying question
here so the user can answer in one pass.)

1. <Question>
2. <Question>
3. …

## 8. Change log

(High-level summary, ≤10 bullets, of every structural change.)

- Reordered sections: Skills moved above Education.
- Cut: high-school details, 2012–2014 retail role.
- Added: "Projects" section with two GitHub links pulled from the user-
  provided text.
- (etc.)
```

---

## Rules for filling the template

- **Never delete a section.** If there is nothing to report, write "No
  findings." Skipping a section breaks the contract with downstream tools.
- **Never reorder sections.** The numbered headings are part of the
  contract.
- **Length budget:** the report should be roughly one printed page of
  scrollable content, plus the change log. If it's longer, the rewrites in
  §5 are probably duplicating findings from §4. Cite findings, don't
  restate them.
- **Truthfulness:** every claim in the report must be supported by the
  resume the user provided. The report is also subject to
  [rewrite-rules.md](./rewrite-rules.md) §1.
