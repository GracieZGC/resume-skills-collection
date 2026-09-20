# Adding Examples

Examples teach by showing how the rules manifest on real resumes. A
strong example is more useful than a long rule essay. New personas
(career changer, bootcamp graduate, contractor, etc.) and stronger
before/after pairs are welcome.

This doc is the recipe.

---

## What counts as a good example

A good example has all three:

1. **A realistic "before".** A flawed resume that a real candidate
   might actually write — not a strawman with every issue piled on.
   The point is to show the skill handling realistic noise.
2. **A correct "after".** The rewrite follows
   [`../resources/rewrite-rules.md`](../resources/rewrite-rules.md)
   strictly. No invented metrics. Every assumption labeled
   `[CONFIRM]` or `[ADD IF TRUE: …]`.
3. **Notes that cite the rules.** `notes.md` explains *why* each
   change happened, with explicit references to the resource files.
   "Cut padding" is not a reason; "Cut the 'Various other tasks as
   needed' bullet per rewrite-rules.md §4 (banned openers)" is.

---

## What disqualifies an example

- **Real people.** Even with permission, anonymized real resumes drift
  back into being identifiable. Use placeholders: `[Company A]`,
  `[University Name]`, `[email]@example.com`. The existing examples
  follow this convention.
- **Invented metrics.** Even in an example, "Reduced latency by 40%"
  without a clear source teaches the wrong lesson. Use
  `[ADD IF TRUE: …]` placeholders in the "after".
- **Strawman "before".** A before-resume with 12 problems in 8 lines
  is parody, not illustration. Stick to 2–4 realistic issues per
  bullet at most.
- **Examples that duplicate an existing persona** without a clear new
  signal. If your example would teach the same lesson as the existing
  `software-engineer/` example, sharpen the existing one instead.

---

## Repo layout for examples

```
examples/<persona>/
├── before.md   # the source resume (flawed, but plausible)
├── after.md    # the skill's rewrite, following all rules
└── notes.md    # what changed, why, citing rules
```

Personas are kebab-cased directories. The README index
([`../examples/README.md`](../examples/README.md)) lists every persona;
add yours to the table when you add the directory.

---

## Recipe for a new persona

1. **Pick the niche.** What's the specific candidate situation that
   isn't covered by an existing persona? Examples of gaps the
   community would benefit from:
   - Career changer (different field → tech)
   - Bootcamp graduate (no CS degree, intensive program)
   - International candidate applying to US-shaped resumes
   - Open-source maintainer with no traditional employer
   - Recovering academic (PhD → industry)
   - Contractor / freelancer with many short engagements
2. **Write a realistic "before".** 200–400 words, 1–3 jobs, the kind
   of issues real candidates in this situation have. Match the
   existing examples' tone.
3. **Write the "after".** Run it mentally through the workflow in
   [`../resources/workflow.md`](../resources/workflow.md). Every
   change must trace to a rule. Use `[CONFIRM]` / `[ADD IF TRUE: …]`
   liberally — they are not weaknesses of the example, they are part
   of the lesson.
4. **Write the "notes".** Number the changes. For each, cite which
   file's which section/rule justifies the change. Add a
   "Questions for the user" subsection that mirrors what the report
   would ask.
5. **Update [`../examples/README.md`](../examples/README.md)** to add
   the persona row to the table.

---

## Style and length

- Keep each file ≤500 lines.
- Use the same markdown structure the existing examples use, so
  diffing across personas is easy.
- Use the same placeholder conventions: `[Person]`, `[Company A]`,
  `[email]@example.com`, `[handle]`, `[CONFIRM: …]`, `[ADD IF TRUE: N]`.
- Plain markdown. No HTML, no embedded images.

---

## How review works

A keyword PR usually merges in a day. An example PR takes longer —
typically one review round to discuss whether the persona is
realistic and whether the rewrite follows the rules. That's normal;
examples are load-bearing teaching material, and a sloppy example
poisons every contributor who reads it later.

If you're unsure whether a persona is worth adding, open an issue
first and ask. Saves both sides time.
