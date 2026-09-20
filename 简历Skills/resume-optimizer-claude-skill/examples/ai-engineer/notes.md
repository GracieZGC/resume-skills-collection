# Notes — AI Engineer

## What changed

1. **"99% accuracy" is a red flag.** A bullet that says "Achieved 99%
   accuracy on classification tasks" is the single most common form
   of fabrication on AI/ML resumes. Without the **dataset**, the
   **evaluation set**, the **baseline**, and the **task definition**,
   a 99% number is meaningless or wrong. The rewrite forces all four
   to be flagged for confirmation — the user almost certainly knows
   the real numbers, but the skill will not ship the original bullet
   as written.
2. **"50% performance improvement" similarly flagged.** Improvement
   *of what*, measured *how*, on *which baseline*? See
   rewrite-rules.md §1. Cannot ship without `[CONFIRM: …]`.
3. **RAG bullet completely restructured.** The "before" said
   "Implemented RAG", which scores 1/5 (every AI engineer "implemented
   RAG" in 2024–25). The rewrite forces the bullet to name the
   corpus, the embeddings, the index, the retrieval strategy, and the
   business outcome. Each is `[CONFIRM]`-marked so the user fills in
   honestly.
4. **Buzzwords cut.** "Cutting-edge AI/ML, deep learning, and LLMs" /
   "state-of-the-art models with significantly improved performance"
   — all buzzwords with no supporting specifics. Replaced with two
   concrete recent projects.
5. **Publication citation flagged for completion.** "A Novel Approach
   to Deep Learning — published 2021" is unusable. The rewrite leaves
   a `[CONFIRM full citation]` placeholder. Per rewrite-rules.md §1,
   the skill cannot invent venue, co-authors, or DOI — that's the
   user's job.
6. **Project given a real shape.** "Built a chatbot using OpenAI API"
   tells nothing. The rewrite requires a real link and a one-sentence
   description; if the user can't fill it, the project may not be
   worth listing.
7. **Skills section grouped.** Cut JAX, Vertex AI, Pinecone, Weaviate,
   Kubernetes, NumPy/pandas (assumed if PyTorch), Jupyter (not a
   skill at this level). Each was either unevidenced or low-signal.
   Gap analysis in the report can re-add anything with real bullet
   support.

## What the report would flag for the user

- **Questions** (workflow step 8): For the classification bullet,
  what's the dataset, baseline, eval set, and the actual metric? For
  the 50% bullet, 50% of what? For the publication, what's the venue,
  full author list, and DOI?
- **Gap analysis** (ai-ml + backend): No mention of model monitoring,
  drift detection, A/B testing on model outputs, or feature stores —
  common gaps in applied ML resumes. Cheap to add if true.

## What did **not** change

- Employer names, dates, degrees — user-owned facts.
- The structural choice to keep both ML roles. Five years is enough
  experience that both belong on a one-page resume.
