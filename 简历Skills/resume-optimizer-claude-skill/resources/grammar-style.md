# Grammar and Style

Step 7 of the workflow. Run **after** bullet rewrites, not before — fixing
grammar on placeholder content is wasted effort.

The rules below are the defaults. When the user's intended style departs
from them (e.g., a UK-English resume, an academic CV), keep the user's
convention and apply it consistently.

---

## Tense

- Past role → past tense throughout.
- Current role → present tense for ongoing responsibilities, past tense for
  completed initiatives within that role. Be consistent within the role.
- A current role that mixes present + past *across the same bullet* is the
  most common error. Fix it.

## Voice

- **Active**, not passive. "Reduced p99 latency 40%." not "p99 latency was
  reduced 40%."
- **No first person.** Drop "I", "my", "we" entirely. They are implied.
- **No articles at the start of bullets.** "Designed and shipped X."
  not "A design and shipping of X."

## Parallelism

Within a section, bullets should be grammatically parallel. The shape is
typically:

> `[verb past-tense] [direct object] [outcome clause].`

If three bullets follow this shape and the fourth is `[Noun phrase]…`,
rewrite the fourth.

Skills sections need parallelism too — if "Languages" is a comma list, so
is every other category. If one is a bulleted list with versions, all are.

## Numerals

- **Digits for 10 and above.** Words for below 10.
- **Always digits for metrics**, regardless of size: `4%`, `9 users`, `2.3M
  requests/day`.
- **Use the metric's natural unit**: `12ms` not `0.012s`.
- **Round to two significant figures** unless the precision matters: `40%`
  not `39.7142%`.
- **Currency**: `$1.2M`, `$450K`. Never bare `1,200,000`.

## Punctuation

- **Oxford comma on.** "Python, Go, and Rust." not "Python, Go and Rust."
- **No terminal periods on single-fragment bullets**, OR period on all
  bullets. Pick one within the resume and apply consistently. Default:
  periods on every bullet (safer for ATS that re-flows whitespace).
- **No double spaces** after periods.
- **Em-dash** with no spaces: `Senior Engineer—Acme` is acceptable; the
  more common convention is spaced en-dash: `Senior Engineer – Acme`. Pick
  one and stick to it.
- **Avoid em-dashes inside date ranges** (parsing landmine, see
  [ats-rules.md](./ats-rules.md)). Use `–` (en-dash) or the literal word
  `to`.

## Capitalization

- **Sentence case** for bullets and summary text.
- **Title Case** for section headings.
- **Proper-noun case** for tools, languages, frameworks: `JavaScript`, not
  `Javascript`; `PostgreSQL`, not `Postgresql`; `Kubernetes`, not
  `kubernetes`.
- **Acronyms in all caps**: `AWS`, `GPU`, `API`. Exceptions: `iOS`, `eBay`.

## Spelling and locale

- Match the user's locale: US English by default, UK English if the user's
  resume already uses it ("optimised", "organisation").
- Spell-check **proper nouns** specifically — typos in employer names and
  tool names are red flags (see
  [recruiter-checklist.md](./recruiter-checklist.md)).

## Word-level cuts

These words add length without adding meaning. Cut them unless they
materially change the bullet.

- "very", "really", "quite", "rather"
- "successfully" (every bullet implies success)
- "significantly", "substantially" (replace with the number)
- "various", "multiple", "numerous" (replace with the count)
- "etc." (commit to the list)
- "in order to" → "to"
- "due to the fact that" → "because"

## Buzzword discipline

These words are not banned, but they need to earn their place by being
backed up elsewhere in the resume:

> synergy · leveraged · utilized · spearheaded (only if user actually led) ·
> dynamic · innovative · world-class · best-in-class · cutting-edge ·
> mission-critical · paradigm · disruptive · holistic · ninja · rockstar ·
> guru · wizard

If a buzzword appears with no supporting evidence, cut it. If it has
evidence, replace it with the evidence:

> ❌ "Leveraged cutting-edge ML to deliver innovative solutions."
> ✅ "Trained a fine-tuned BERT model that improved support-ticket
> classification accuracy from 71% to 89%."
