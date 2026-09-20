# Notes — Software Engineer (mid-level)

## What changed

1. **Title de-inflated.** "Lead Senior Software Engineer II" is a
   composite title that doesn't exist at most companies — recruiter
   red flag (see recruiter-checklist.md "Job titles that don't exist").
   Restored to "Software Engineer II", which is plausible and matches
   what LinkedIn would show.
2. **Buzzwords cut.** "robust, scalable, mission-critical" /
   "passionate" / "clean code, agile methodologies, high-quality
   solutions" — every word from grammar-style.md's "Buzzword
   discipline" list. Replaced with a 2-line summary naming the actual
   technologies and the actual recent work.
3. **ATS landmine fixed.** The "before" Skills section is a 4-column
   markdown table. Tables for layout fail ATS parsing (ats-rules.md
   Hard Rule §1). Replaced with a flat, grouped list.
4. **Banned openers removed.** "Lead", "Owns…is responsible for",
   "Worked on…significantly", "Was responsible for", "Various other
   tasks as needed" — five distinct issues, all addressed.
   "Significantly" without a number is invisible — replaced with a
   placeholder.
5. **Tense fixed.** "Lead the development", "Mentored", "Owns",
   "Worked on" mixed present and past in the current role. Normalized
   to present tense for ongoing work, past tense for completed
   initiatives within the role (per grammar-style.md "Tense").
6. **Scope added everywhere.** Each bullet now answers: what was built,
   in what language, who used it, and (if known) what changed for
   them. Where the user almost certainly has the number but didn't
   include it, `[ADD IF TRUE: …]` flags it for the report.
7. **Cloud claim flagged.** The "before" lists AWS, GCP, and Azure
   together. Production multi-cloud experience at 4 years is unusual;
   the rewrite picks AWS as the most likely true claim and marks the
   rest as `[CONFIRM scope]`. The skill never deletes a user's claim
   silently — it surfaces the verification.

## What the report would flag for the user

- **Questions** (workflow step 8): What's your actual GCP / Azure /
  Kubernetes / Terraform scope — production, dev environments, side
  project, or coursework? What metric improved most after the CI/CD
  parallelization?
- **Gap analysis** (backend domain): No observability terms
  (Prometheus, OpenTelemetry, Datadog) and no message-queue exposure.
  If true gaps, they're the most cost-effective next investments. If
  false gaps, surface them in a bullet.

## What did **not** change

- Employer names, dates, school — user-owned facts.
- The migration narrative (monolith → microservices) preserved; only
  rewritten to explain *what got better* rather than restate the
  activity.
