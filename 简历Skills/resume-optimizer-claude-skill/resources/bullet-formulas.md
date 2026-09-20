# Bullet Formulas

Every bullet rewrite uses one of the three formulas below. Pick by what the
source bullet already contains; do not force a formula that requires
information the user did not provide.

The formulas are scaffolding, not templates — once a bullet is written,
re-read it as a human sentence and cut any glue words ("in order to",
"which resulted in", "by means of") that the formula left behind.

---

## X-Y-Z (Google's formula)

> **"Accomplished [X] as measured by [Y] by doing [Z]."**

Use when the source bullet has both an outcome and the action that drove it.
Best for senior or impact-heavy bullets.

**Examples**

- Accomplished **a 40% reduction in checkout latency** as measured by **p99
  response time over 30 days** by **rewriting the cart service to use Redis
  caching and async order writes**.
- Accomplished **$1.2M in annualized infra savings** as measured by **AWS
  monthly billing** by **migrating the analytics pipeline from EMR to a
  Spark-on-EKS cluster**.

**Anti-pattern** — using X-Y-Z when no Y exists. Don't pad with a fake
metric ("as measured by improved team velocity").

---

## CAR (Challenge — Action — Result)

> **"[Action verb] [Action] to [solve Challenge], [Result]."**

Use when the source bullet has a clear problem the user solved, but the
metric is qualitative or scoped (not a single number).

**Examples**

- Designed and shipped a **typed event schema registry** to eliminate
  recurring data-pipeline outages caused by upstream schema drift, **cutting
  pipeline incidents to zero over the following quarter**.
- Led the **post-mortem and remediation of a 4-hour production outage**,
  introducing canary deploys and synthetic monitoring that **caught two
  subsequent regressions before customer impact**.

**Anti-pattern** — burying the action in a noun phrase ("Was responsible
for the design of…"). Open with the verb.

---

## STAR (Situation — Task — Action — Result)

> **"In [Situation], tasked with [Task], [Action verb] [Action], [Result]."**

Use when the bullet needs context the rest of the resume doesn't carry.
Often the right choice for project bullets, research bullets, or
career-pivot bullets where the role title alone doesn't explain the work.

**Examples**

- During a 3-month rotation on the security team, tasked with reducing
  high-severity vulns in the auth service, **patched 12 CVEs and shipped a
  mandatory MFA flow**, lowering the team's open-vuln backlog from 38 to 6.
- For a graduate research project on protein-ligand affinity, **trained and
  evaluated a graph neural network against three published baselines on the
  PDBbind v2020 dataset**, matching state-of-the-art RMSE within 0.05.

**Anti-pattern** — STAR-ifying every bullet. Most experience bullets do not
need Situation and Task; the section heading already provides them.

---

## Verbs first, glue words last

After picking a formula:

1. Cut "in order to" → "to".
2. Cut "which resulted in" → ", [result]" (comma + result clause).
3. Cut "by means of" → "by".
4. Cut articles at the start of bullets ("The", "A", "An").
5. Cut self-references ("I", "my", "we").

A finished bullet should fit on **one or two lines**. If it spans three,
either the bullet is two bullets, or it has padding to remove.

---

## When the source has no result

If the user-provided text genuinely has no outcome to point to:

- **Don't invent one.** See [rewrite-rules.md](./rewrite-rules.md) §1.
- **Add a `[ADD IF TRUE: …]` placeholder** for the kind of metric that
  would belong there. Example:
  > Built an internal feature-flag service used by [ADD IF TRUE: N teams /
  > N services], reducing per-feature release coordination time.
- **Mention it in the report's "Questions for the user" subsection** so the
  user can answer in one pass.

A bullet that lives without a result is acceptable — a fabricated result
is not.
