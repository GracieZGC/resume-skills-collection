# Resume Optimization Workflow

The skill runs the 10 steps below in order. Each step is small, observable,
and produces an artifact the next step consumes. Do not skip steps; do not
merge them. If a step has nothing to flag, say so explicitly in the report
(silence is ambiguous).

---

## 0. Intake (implicit prerequisite)

Before step 1, the user must have provided **resume text**. If the user only
described their background without pasting a resume, ask for the resume text
(or a path the host can read). Do not run the workflow on a verbal summary.

If the user has a target role or job description, capture it. Tailoring
(step 9) is materially better when the target is known. If absent, infer the
domain from the resume's strongest signal and state the inference.

---

## 1. Extract structure

Identify and label the sections present:

- Header / contact
- Summary / objective (if present)
- Experience
- Education
- Skills
- Projects
- Publications, patents, talks (if research-oriented)
- Certifications, awards, volunteering, languages

Note **missing** standard sections and **non-standard** sections. Section
order matters for ATS and for recruiter scan — record the current order.

## 2. Analyze formatting

Flag anything that hurts machine parsing or human scanning. Use
[ats-rules.md](./ats-rules.md) as the checklist:

- Tables/columns used for layout
- Text boxes, icons, images standing in for words
- Headers/footers carrying contact info
- Non-standard section headings
- Inconsistent date formats
- Inconsistent capitalization, fonts (if visible), or bullet glyphs

Do not rewrite yet — list the findings.

## 3. Analyze ATS compatibility

Run the ATS-specific checks on top of formatting:

- Is contact info in the body, not the header/footer?
- Are job titles, employers, and dates discoverable line-by-line?
- Are skills written as the words a recruiter or ATS would search?
- Are there parsing landmines: ligatures, special characters, em-dashes
  inside dates, mixed bullet glyphs?

Output: a short list of ATS risks ranked high/medium/low.

## 4. Score every section

Apply [scoring-rubric.md](./scoring-rubric.md). Each section gets a 0–5 score
and a one-line reason. Do not skip sections that scored 5/5; their score
anchors the report.

## 5. Detect weaknesses

For each section scored ≤3, list the specific weakness(es) and which rule(s)
in [rewrite-rules.md](./rewrite-rules.md) they violate.

Cross-section weaknesses also belong here:

- Resume length
- Voice/tense inconsistency
- Missing or weak summary
- Skills section disconnected from experience bullets

## 6. Rewrite bullets

For each weak bullet (or every bullet, if the user asked for a full
rewrite), produce a rewrite using:

- [bullet-formulas.md](./bullet-formulas.md) for structure
- [action-verbs.md](./action-verbs.md) for openers
- [rewrite-rules.md](./rewrite-rules.md) §1 for anti-fabrication

Use the `[CONFIRM]` / `[ADD IF TRUE]` markers from rewrite rule §2 when a
rewrite leans on something the user must verify. Never silently insert
numbers.

## 7. Improve grammar

Apply [grammar-style.md](./grammar-style.md): tense, parallelism, numerals,
articles, Oxford comma. This step runs after step 6 because grammar fixes
on placeholder content are wasted work.

## 8. Suggest measurable achievements (without inventing)

Where a bullet is qualitative and the user *might* have a metric to add,
generate a question or a `[ADD IF TRUE: …]` placeholder. Examples:

- "How many users did this serve at peak?"
- "Was this rolled out company-wide or to a single team?"
- "Did this change a measurable number — latency, conversion, cost, build time?"

Group these as a "Questions for the user" subsection of the report so they
are easy to answer in one pass.

## 9. Optimize for the inferred (or stated) target role

- Pick the keyword file: [keywords/](./keywords/) by domain.
- Compare the resume's vocabulary against the file.
- For each missing keyword, decide:
  - User has the experience → reword existing bullet to surface the keyword.
  - User does not → do not add. Note as a gap in the report.
- Reorder sections / bullets so the most role-relevant signal is first.

If a job description was provided, additionally extract its top
~15 keywords/skills and run the same gap analysis against the resume.

## 10. Produce the final resume and report

Two artifacts, always both:

1. **Final resume**, fully rewritten, ATS-safe, ready to paste back into a
   `.docx` template. Plain markdown with standard headings is the
   interchange format.
2. **Report**, following [report-template.md](./report-template.md): scores,
   findings, change log, gap analysis, questions for the user.

The report is not optional. A rewrite without a report is a black box.
