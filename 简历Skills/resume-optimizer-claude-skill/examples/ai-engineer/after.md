# [AI Engineer]

[city] · [email]@gmail.com · linkedin.com/in/[handle] · github.com/[handle]

## Summary

ML engineer, 5 years, productionizing LLM and classical-ML features.
Recent focus: a RAG system over the company's internal docs and a
classification pipeline that replaced a hand-tuned heuristic.

## Experience

**Machine Learning Engineer**, [Company A] — Jun 2022 – Present

- Built a retrieval-augmented generation (RAG) system over [CONFIRM:
  the internal support-docs corpus, ~N documents], using [CONFIRM:
  text-embedding-3-small] embeddings, pgvector, and hybrid search
  (BM25 + cosine); answers [ADD IF TRUE: N% of] support tickets without
  escalation.
- Productionized a [CONFIRM: ticket-priority] classifier (DistilBERT
  fine-tune on [ADD IF TRUE: N labeled examples]); replaced a rules
  engine [CONFIRM: improved F1 from X to Y, measured on a held-out
  set of Z examples].
- Built the team's prompt-evaluation harness: pairwise LLM-as-judge
  evals run in CI on every prompt change, with a [ADD IF TRUE:
  human-rated golden set of N pairs] for calibration.

**ML Engineer**, [Company B] — May 2020 – May 2022

- Trained and deployed [CONFIRM: 4] PyTorch models for [CONFIRM:
  product-similarity ranking]; served via TorchServe behind a FastAPI
  gateway.
- Cut training time on the recommendation model [ADD IF TRUE: from X
  hours to Y hours] by moving from single-GPU to FSDP across 4 A100s.
- Set up MLflow tracking and a model registry; replaced ad-hoc
  notebook-to-prod handoffs that the team had been doing manually.

## Projects

**[Project name]** — github.com/[handle]/[repo] (open source)

- Built a [one-sentence description] using [stack]; [ADD IF TRUE:
  stars / downloads / contributors] indicator if material.

## Education

**[University]** — M.S. Computer Science, 2020
**[University]** — B.Tech Electronics, 2018

## Publications

- [CONFIRM full citation: Authors, "A Novel Approach to Deep Learning",
  Venue, Year, DOI/URL]. The skill cannot publish a polished citation
  without the venue and author list — request these in the report.

## Skills

- **Languages:** Python, SQL
- **ML frameworks:** PyTorch, Hugging Face Transformers, scikit-learn,
  XGBoost
- **LLM tooling:** OpenAI / Anthropic APIs, LangChain, pgvector, FAISS,
  prompt evaluation
- **Training:** FSDP, mixed precision, MLflow, Weights & Biases
- **Infra:** Docker, Kubernetes, AWS SageMaker, FastAPI / TorchServe
