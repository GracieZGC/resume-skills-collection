# Adding Keywords

Adding to the domain keyword vocabularies is the highest-leverage,
lowest-friction contribution to this project. If you've been on either
side of a recent hiring loop and noticed terms that recruiters search
but aren't in the relevant file, please open a PR.

This doc is the recipe.

---

## Where the keyword files live

`resources/keywords/`, one file per domain:

- `software-engineering.md` — generic SWE
- `backend.md`
- `frontend.md`
- `ai-ml.md`
- `devops.md`
- `cloud.md`
- `data-science.md`
- `research.md`

Each file is a categorized list. The skill loads exactly one (or
sometimes two) of these per resume review, picked by the strongest
signal in the resume.

---

## Criteria for adding a keyword

A keyword belongs in a domain file if it satisfies **all three**:

1. **Recruiters search for it.** If a recruiter wouldn't paste it into
   an ATS search bar, it's not a keyword — it's trivia.
2. **It's a noun (or noun phrase) candidates can plausibly claim.**
   Verbs and concepts belong elsewhere (`action-verbs.md` or
   `bullet-formulas.md`).
3. **It's stable enough to be useful.** Brand-new project names
   shipping their first 1.0 next month don't belong in a domain file
   yet. Wait for the term to settle.

If a keyword is borderline, it doesn't belong. The cost of a stale or
noisy keyword is real — the skill nudges candidates to surface it,
which can make a resume look dated or buzzword-padded.

---

## Criteria for **not** adding a keyword

Skip keywords that:

- **Are tools that aren't searched for.** Notion, Slack, Confluence,
  JIRA — every team uses them. They are not skills.
- **Are buzzwords.** "Cutting-edge", "best-in-class", "synergy" —
  these belong on the cut list in `grammar-style.md`, not in any
  keyword file.
- **Are generic methodologies.** "Agile", "Scrum", "Kanban" — every
  team claims these. Recruiters do not search for them.
- **Already appear** in a more general file. If a keyword is in
  `software-engineering.md`, don't duplicate it into `backend.md`
  unless the backend-specific framing is genuinely different.

---

## How to structure your addition

1. Find the right file (and the right section within the file).
2. Add the term in alphabetical-within-section order, separated by
   ` · ` (middle dot) like the existing entries.
3. If the term needs a new section, add the section header (`## Foo`)
   in a place that fits the file's existing ordering.
4. If you're adding more than ~10 terms, open the PR with a short
   description of where the additions come from (your hiring loop, a
   specific JD set, etc.) so reviewers can sanity-check.

Example diff:

```diff
 ## Languages — Python data stack

-pandas · NumPy · Polars · Dask · Modin · Vaex · SciPy
+pandas · NumPy · Polars · Dask · DuckDB · Modin · Vaex · SciPy
```

---

## Testing your addition

You don't need to run any tests. The skill loads keyword files as plain
markdown — there's no schema to break. The CI workflow does run
`markdownlint` on the file (see `.github/workflows/lint.yml`), so make
sure your markdown is well-formed.

If you'd like to **prove** the keyword improves a real review, run the
skill against one of the example "before" resumes for the relevant
domain and check whether the new keyword gets correctly surfaced.

---

## A note on locale and seniority

Some keywords are more relevant in specific markets (US vs. EU vs.
APAC) or at specific seniority levels. When a term is clearly
locale-bound (e.g., "Form ADV" is a US-specific compliance term),
group it under a clearly-named subsection so the skill knows it's
context-dependent.

For seniority-bound terms (e.g., "principal-level architecture
ownership"), prefer rewriting [`bullet-formulas.md`](../resources/bullet-formulas.md)
or [`action-verbs.md`](../resources/action-verbs.md) instead — these
aren't keywords, they're patterns.
