# Notes — Senior Engineer

## What changed

1. **Summary specific, not heroic.** "Highly experienced…
   mission-critical…innovative, disruptive…proven track record" is
   four buzzwords in 30 words. Replaced with a 2-line summary that
   names the level (Principal), the org scope, the recent technical
   initiative, and team growth. Senior summaries earn the read by
   being specific, not by being adjectives.
2. **"Various responsibilities" deleted everywhere.** Every senior
   resume has at least one of these. They communicate that the
   candidate isn't sure which work was important. Cut and replaced
   with the strongest 1–2 bullets per role.
3. **Bullet count cut by seniority.** The "before" had near-identical
   bullet count per role going back 12 years. Recent roles are
   important; the intern from 2009 is not. Internship is removed
   entirely (rewrite-rules.md §8); the 2010–2012 role gets one
   bullet, 2013–2016 gets two, 2016–2020 gets three, current role
   gets four. The shape of the section now matches the candidate's
   actual signal.
4. **Leadership without inflation.** Senior bullets often inflate
   verbs — "Led", "Drove", "Owned" used three times each in the
   "before". Where the user genuinely had the authority, the verb
   stays; where the work was more accurately collaborative, the
   verb changes to `Co-authored`, `Mentored`, `Partnered`. The
   skill cannot tell the difference from the resume alone — it
   flags suspicion in the report rather than silently downgrading.
5. **Architectural specifics added.** "Service mesh", "gRPC + Istio",
   "Spanner", "feature-flag platform", "search-indexing pipeline" —
   these are the terms a recruiter searching for a Principal
   candidate types in. They were absent from the "before" entirely
   (only in skills). Surfaced into bullets per backend.md.
6. **Skills section restructured.** The "before" presumably listed
   every tech in 12 years. The rewrite lists only what the candidate
   has used **recently and at depth** — recruiters skim skills
   sections for evidence of current capability, not career
   archaeology.
7. **Internship removed.** A 2009 intern role on a 2026 senior
   resume contributes nothing. Cut per rewrite-rules.md §8.

## What the report would flag for the user

- **Questions** (workflow step 8): Team size at Company A?
  Migration outcomes (downtime, breakage, traffic)? Adoption
  numbers for the feature-flag platform? Search-pipeline QPS and
  latency? MAU on the launch at Company D?
- **Gap analysis** (backend + leadership): No mention of
  hiring/headcount-management metrics, retention, or specific
  promotion outcomes — common gaps in senior resumes that
  hiring managers ask about.

## What did **not** change

- Employer names, dates, school, degree year — user-owned facts.
- Career chronology — kept reverse chronological with the
  weighting adjusted by seniority of the role.
