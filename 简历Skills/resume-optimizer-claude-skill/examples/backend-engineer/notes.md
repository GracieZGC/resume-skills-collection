# Notes — Backend Engineer

## What changed

1. **Summary made specific.** "Scalable distributed systems using modern
   technologies" tells a recruiter nothing. The rewrite names the
   language (Go), the substrate (Kafka), and the recent work (latency
   + protocol migration). Specificity is what gets the forward.
2. **Every bullet got scope and depth.**
   - "Built microservices in Go" → "Designed and shipped 3 Go services
     on K8s that process [N billion] events per day".
   - "Reduced latency" / "Improved throughput" — invisible. Replaced
     with placeholder for the metric **and** the mechanism (Redis
     cache, pool tuning). The mechanism is on the resume regardless of
     whether the number gets filled in — it shows depth.
   - "Migrated from REST to gRPC" → added the migration *strategy*
     (Envoy proxy, incremental adoption), which is what differentiates
     a senior bullet.
3. **Backend-keyword surfacing.** The "before" listed `outbox pattern`,
   `idempotency`, `exactly-once`, `SLO`, `error budget` nowhere in
   bullets, only in (an implied) skills section. Recruiters search
   experience bullets, not skill chips — the rewrite moves these terms
   into the bullets where they belong, and only **because the work
   plausibly involved them** (anti-fabrication still holds; flagged
   with `[CONFIRM]` where unsure).
4. **Skills section restructured by category.** The "before" was one
   28-item alphabetical-ish list — recruiters skim categories. Cut
   technologies that have no bullet-level support (`RabbitMQ`, `NATS`,
   `MySQL`, `Cassandra`, `Elasticsearch`, `GCP`, `Jaeger`, `Java`,
   `Rust`, `GraphQL`) per rewrite-rules.md §7 — "If the user does not
   have the experience, do not add. Note as a gap." These will be
   flagged in the report's gap analysis if the user wants them back.
5. **Education moved below Experience.** 5 years' experience puts the
   degree below the work.

## What the report would flag for the user

- **Questions**: What's your actual daily-event volume? p99 before /
  after the cache change? On-call MTTR delta? Migration duration?
- **Gap analysis** (backend domain): The "before" listed several
  technologies cut for lack of evidence. If any are true and have a
  supporting bullet, re-add them. Specifically worth re-checking:
  RabbitMQ vs Kafka, Cassandra/DynamoDB, Elasticsearch, GraphQL.
- **Cross-cutting**: The user could probably write a stronger summary
  by naming the *scale* (events/day, services, RPS) in the first line.

## What did **not** change

- Employer names, dates, school.
- The two roles' structural narrative — current role still leads, prior
  role still has its migration story.
