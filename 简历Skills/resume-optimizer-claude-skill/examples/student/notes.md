# Notes — Student

## What changed

1. **Header** — Removed street address (unnecessary, privacy risk).
   Swapped a personal "coolcoder99@hotmail.com" address for a school
   email (recruiter-checklist.md red flags). Added LinkedIn and GitHub
   inline.
2. **Objective removed.** A new candidate's resume does not need an
   objective. Scoring-rubric anchor: Objective sections at 2025-era
   resumes score 1/5 when they start with "Seeking a challenging…".
3. **Education** — Trimmed the coursework list from 14 entries to 5
   relevant courses. Calculus III, Public Speaking, English Composition
   do not help a SWE internship application; they look like padding.
4. **Experience bullets rewritten.** Removed "Was responsible for…",
   "Helped with…", "Worked on…", "Participated in…" — every banned
   opener from action-verbs.md. Replaced with `Contributed`, `Closed`,
   `Participated` (in active voice with scope). Used `[ADD IF TRUE: N]`
   for counts the student likely knows but didn't include. Did **not**
   invent ticket counts or PR counts.
5. **Projects rewritten.** Each project now states what was built, the
   stack, and a measurable surface (endpoint count, components, etc.).
   Added GitHub links — the student already has the repos; surfacing
   them is the lazy win.
6. **Skills trimmed.** Cut Go/Rust/Kotlin/Swift/PHP/Ruby/MATLAB/R — a
   sophomore listing 15 languages is a credibility hit. Cut Microsoft
   Office (not a skill at this level), all "Soft Skills" (every resume
   claims these; they're noise). Grouped remaining skills.
7. **High school removed.** Per rewrite-rules.md §8: drop high-school
   details once the user has begun a degree, unless the school is
   exceptional and recent.

## What the report would flag for the user

- **Questions for the user** (from workflow step 8): How many React
  components did you build on the redesign? How many bug tickets did
  you close? Where is the portfolio deployed?
- **Gap analysis** (workflow step 9, software-engineering domain): No
  resume-visible exposure to testing (pytest/Jest/Vitest), CI/CD, or
  databases used in production. Suggest adding a 5-line "Database
  Systems coursework — built [project]" project if true.

## What did **not** change

- GPA stayed (3.4 is borderline-helpful; left to the student to decide).
- Internship company name and dates are user-owned facts; preserved
  verbatim.
- No metrics were invented to "strengthen" the bullets.
