# Usage

The skill is designed to need **no special prompting**. Paste a resume,
say what you want, and the skill produces a rewrite plus a structured
report.

This doc covers:

- The activation triggers
- What input you should provide
- What output to expect
- Common follow-up prompts
- Troubleshooting

---

## Activation triggers

The skill activates on any of these patterns (case-insensitive):

- "Improve my resume" / "Review my CV" / "Rewrite my resume"
- "ATS optimize my resume" / "Make this ATS-friendly"
- "Resume feedback" / "Score my resume" / "Critique my resume"
- "Tailor my resume to <role / JD>"
- "Make this recruiter friendly"
- "Optimize for software engineering / AI / backend / frontend / DevOps
  / cloud / data science / research jobs"

The skill also activates implicitly when a resume is pasted with no
instruction — it will default to a full review.

If you want **just one part** of the workflow (e.g., "only score, don't
rewrite"), say so. The skill will still run the workflow steps that
support your request and skip the others.

---

## What to provide

The skill always needs:

1. **The resume text.** Paste it directly into the chat. If you have a
   PDF or DOCX, the optional MCP server can extract the text; otherwise
   copy/paste from the source document.

Optional but recommended:

2. **A target role or job description.** "Tailor this for a Staff
   Backend role at a fintech." A pasted JD is even better. With a
   target, the skill's gap analysis (workflow step 9) is much sharper.
3. **Any specific concerns.** "I'm worried about a 9-month gap" or
   "My title was inflated; do I cut it?" The skill will address these
   in the report.

The skill will **not** invent or infer the following:

- Metrics you didn't include — they'll come back as `[ADD IF TRUE: …]`
  placeholders or as questions in the report.
- Companies, employers, dates, degrees — these are yours to write.

See [`../resources/rewrite-rules.md`](../resources/rewrite-rules.md) §1.

---

## What you get back

Every full run returns **two artifacts**, separated by `---`:

1. **The rewritten resume** in plain markdown, with standard section
   headings. Ready to paste into a `.docx` template.
2. **A structured report**, following the shape in
   [`../resources/report-template.md`](../resources/report-template.md).
   Sections (in fixed order):
   1. Scores
   2. Formatting findings
   3. ATS findings
   4. Section-level weaknesses
   5. Bullet rewrites (before / after / why)
   6. Gap analysis
   7. Questions for the user
   8. Change log

If you only got one of the two artifacts back, see Troubleshooting.

---

## Common follow-ups

After the first response, useful follow-up prompts:

- "Answer the questions in section 7 of the report" — paste the
  answers, and the skill will fold them into a second-pass rewrite,
  resolving every `[CONFIRM]` / `[ADD IF TRUE]` placeholder.
- "Make it one page" — the skill will cut the lowest-signal content.
- "I'd like the summary punchier" — single-section follow-ups are fine;
  the skill remembers the prior context.
- "Now tailor it to this JD: <paste>" — runs step 9 again with the new
  target.
- "Why did you change <bullet>?" — the report should already explain
  this in §8 (change log) and §5 (bullet rewrites). If not, ask.

---

## Troubleshooting

### The skill didn't activate

- Are you sure it's installed in the host you're using? See
  [`installation.md`](./installation.md).
- Did you paste resume text, or just describe your background? The
  skill needs the actual resume.
- Try an explicit trigger: "Use the resume-optimizer skill to review
  this resume."

### It produced only the rewrite, not the report

That's a bug — the skill's output contract guarantees both. Report it
via [the issue tracker](https://github.com/Sumukhmg/resume-optimizer-claude-skill/issues)
with the prompt you used.

### It invented a metric

That's a serious bug. The anti-fabrication rule is the most important
rule in the skill. **Please report it** via Issues with the prompt and
the offending bullet. We will treat it as a release blocker.

### It changed my employer name / dates / degree

Same as above. Names, dates, degrees, and titles are user-owned facts.
Any silent edit is a bug — report it.

### It refused to rewrite

The skill blocks the rewrite when fabrication is suspected (see
[`../resources/scoring-rubric.md`](../resources/scoring-rubric.md)
"Cross-cutting modifiers"). Read the report's findings — typically a
metric in the original resume doesn't pass smell-test review and the
skill flagged it.
