# [Backend Engineer]

[city] · [email]@gmail.com · linkedin.com/in/[handle] · github.com/[handle]

## Summary

Backend engineer, 5 years, working on event-driven services in Go and
Kafka. Recent focus: latency reduction on the core read path and the
REST→gRPC migration.

## Experience

**Senior Backend Engineer**, [Company A] — Jan 2023 – Present

- Designed and shipped 3 Go services on Kubernetes that process
  [CONFIRM: ~N billion] Kafka events per day, with exactly-once
  semantics via the outbox pattern.
- Cut p99 read latency on the [CONFIRM: account-lookup | catalog]
  service from [ADD IF TRUE: X ms to Y ms] by introducing a Redis
  read-through cache and tuning PostgreSQL connection pooling.
- Owned the on-call rotation for the team's 6 services; authored
  runbooks that reduced average MTTR for paging incidents [ADD IF
  TRUE: from X to Y].

**Backend Engineer**, [Company B] — Aug 2020 – Dec 2022

- Led the migration of the public API from REST to gRPC over [CONFIRM:
  6 months], shipping a parallel Envoy-based proxy that let mobile
  clients adopt gRPC incrementally without breaking REST consumers.
- Built the team's first Datadog dashboards and SLOs for the API
  gateway; established error-budget tracking that became the basis for
  release-go/no-go decisions.
- Replaced an ad-hoc retry layer with idempotency keys + exponential
  backoff, eliminating a recurring duplicate-charge class of bugs in
  the payments path.

## Skills

- **Languages:** Go, Python, SQL, Bash
- **Distributed systems:** Kafka, gRPC, REST, Envoy, outbox pattern,
  idempotency, exactly-once semantics
- **Data:** PostgreSQL, Redis, DynamoDB (read path)
- **Infra:** Kubernetes, Docker, AWS (EKS, RDS, S3), Terraform
- **Observability:** Datadog, Prometheus, OpenTelemetry, SLO / error
  budgets

## Education

**[University]** — B.S. Computer Engineering, 2020
