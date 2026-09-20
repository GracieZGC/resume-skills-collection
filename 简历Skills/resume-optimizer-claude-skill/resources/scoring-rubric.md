# Scoring Rubric

Each section of the resume gets a score from **0 to 5**. Use whole numbers
only — half-points are noise.

The scale is anchored: 3 is the bar for a working professional resume, 5 is
what a top-tier candidate ships. Below 3 always blocks the rewrite for that
section.

| Score | Meaning |
|------:|---------|
| **5** | Top decile. Specific, quantified, role-aligned, ATS-safe. |
| **4** | Strong. Minor polish only; no structural fix needed. |
| **3** | Acceptable. Communicates the role but missing impact, metrics, or focus. |
| **2** | Weak. Vague, generic, or padded. Needs rewriting. |
| **1** | Damaging. Hurts the candidate (typos, false signals, wrong tense, missing dates). |
| **0** | Section is missing or unreadable when it should exist. |

---

## Section-specific anchors

### Header / contact

- **5** — Name, location (city/state/country), one phone, one professional
  email, LinkedIn URL, portfolio/GitHub if relevant. No photo, no DOB, no
  marital status. All in the body, not the header.
- **3** — Has the basics but in a header/footer or with a personal email
  (`coolguy99@…`).
- **1** — Missing email or phone, or contains content that creates bias risk
  (photo, age, nationality where not required).

### Summary / objective

- **5** — 2–3 lines, role-specific, leads with strongest credential, includes
  one signal metric or scope.
- **3** — Present but generic ("Motivated engineer seeking…").
- **1** — Objective statement from 2005 ("Seeking a challenging position
  where I can grow…").
- **0** — Missing when the resume has >5 years experience and would benefit
  from one. For new grads, no summary is fine; do not penalize.

### Experience

Score each bullet, then aggregate the section.

- **Bullet 5** — Starts with strong verb, has scope (what / how much), has
  outcome (measurable result), is ≤2 lines.
- **Bullet 3** — Strong verb and scope, no outcome. Or outcome but no scope.
- **Bullet 1** — "Responsible for…", "Worked on…", or pure tool-name list.

Section score = floor(average bullet score), with these caps:
- Cap at 4 if any bullet is ≤2.
- Cap at 3 if any bullet has a tense mismatch.
- Cap at 3 if the section lacks dates or locations.

### Education

- **5** — Degree, institution, graduation date, honors/GPA *only if strong
  and recent*. Relevant coursework only for new grads.
- **3** — Has degree + institution + date but missing honors that would help,
  or includes high school after a degree.
- **1** — Missing graduation date, or GPA listed when it actively hurts.

### Skills

- **5** — Grouped by category (Languages, Frameworks, Infra, Tools), uses the
  exact terms recruiters search, every listed skill is supported by an
  experience or project bullet.
- **3** — Flat list, but plausible and supported.
- **1** — Padded with non-skills ("Microsoft Word", "teamwork",
  "problem solving"), or lists skills not evidenced anywhere else.

### Projects

- **5** — Each project has: name, link, one-line problem statement, your
  contribution, outcome or scale, tech used.
- **3** — Name + tech but no contribution or outcome.
- **1** — Only tech tags, no description of what was built.

### Research-specific (Publications, Patents, Talks)

- **5** — Consistent citation format, full author list, venue, year, DOI/URL.
- **3** — Present and complete but inconsistent format.
- **1** — Author order obscured, venues missing, or self-published mixed
  with peer-reviewed without distinction.

---

## Cross-cutting modifiers

After scoring sections, apply these caps to the **overall** resume signal in
the report (not to individual sections):

- **Length wrong for experience level**: cap overall at 3.
- **Inconsistent tense across the resume**: cap overall at 3.
- **Any fabricated content suspected** (a metric or claim the user later
  cannot defend): block the rewrite and flag it before any further work.
- **ATS landmines from [ats-rules.md](./ats-rules.md)** present: cap overall
  at 3 until resolved.
