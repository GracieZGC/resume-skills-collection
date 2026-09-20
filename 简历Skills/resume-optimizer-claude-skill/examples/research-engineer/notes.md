# Notes — Research Engineer

## What changed

1. **Research interests trimmed.** "Machine learning, deep learning,
   computer vision, NLP, AI for science, and anything related to AI"
   says the candidate has no focus. The rewrite narrows to three
   coherent areas pulled from the user's actual work history.
2. **Publications expanded into real citations.** "Our paper —
   NeurIPS 2024" is unusable. The skill cannot ship a citation
   without the full author list, the full title, and a DOI/URL.
   `[CONFIRM]` slots force the user to fill these in — see
   rewrite-rules.md §1 and scoring-rubric.md "Research-specific".
3. **"Several other papers" forbidden.** A research CV must enumerate
   every publication or explicitly state which categories were
   omitted (e.g., "Selected publications below; full list at
   [Google Scholar URL]"). Vague aggregation is a 1/5 finding.
4. **NeurIPS 2024 bullet given depth.** "Published a paper at NeurIPS"
   tells nothing about the candidate's contribution. The rewrite
   forces them to specify author position (`first / shared first /
   co-author`), the role they played (model, training, evaluation,
   ablations), and the technical content — `[CONFIRM]` for each.
   Author position is one of the highest-signal facts on a research
   CV; never let it stay implicit.
5. **Thesis title and advisor added.** Both expected on a research CV.
   Absence is a recruiter red flag.
6. **Selected service section added.** Peer review, workshop
   organization, and similar service signals are common on research
   CVs and often forgotten. Added an `[ADD IF TRUE]`-gated section.
7. **No length penalty applied.** Per research.md (keywords): research
   CVs are exempt from the one-page rule in scoring-rubric.md
   "Length wrong for experience level".

## What the report would flag for the user

- **Questions** (workflow step 8): Author position on each
  publication? Full titles? Thesis advisor and committee?
  Reviewing history? Talks given?
- **Gap analysis** (research + ai-ml): No mention of grants, awards,
  invited talks, or teaching — common on research CVs and often
  load-bearing for the next career step. Cheap to add if any are true.
- **Cross-cutting**: Consider adding a "Selected talks" section if the
  user has invited talks or conference presentations distinct from
  paper publications.

## What did **not** change

- Degree institutions, dates, and the order of education.
- The structural choice to keep the PhD as its own job-style entry —
  for research engineers this is standard; for industry-only candidates
  it would fold under Education.
