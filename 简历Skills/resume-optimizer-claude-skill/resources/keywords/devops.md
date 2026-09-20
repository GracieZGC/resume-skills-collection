# DevOps / SRE / Platform Engineering Keywords

Vocabulary for DevOps engineer, SRE, platform engineer, and infrastructure
roles. Used in workflow step 9 when the target is ops/platform-shaped.

**Usage:** add keywords **only when supported by the user's experience**.
See [rewrite-rules.md](../rewrite-rules.md) §7.

For adjacent roles, branch:
- Cloud provider depth → [cloud.md](./cloud.md)
- Backend services using the infra → [backend.md](./backend.md)

---

## CI/CD

GitHub Actions · GitLab CI · CircleCI · Jenkins · TeamCity · Bamboo ·
Argo CD · Argo Workflows · Argo Rollouts · Flux CD · Spinnaker ·
Buildkite · Drone CI · Tekton · Concourse · Continuous integration ·
Continuous delivery · Continuous deployment · Trunk-based development ·
Feature flags · LaunchDarkly · Split.io · Unleash · Blue/green
deployment · Canary deployment · Rolling deployment · Shadow deployment

## Infrastructure as Code

Terraform · OpenTofu · Pulumi · CloudFormation · CDK · Bicep · Ansible ·
Chef · Puppet · SaltStack · Crossplane · Helm · Helmfile · Kustomize ·
Packer · Vagrant

## Containers and orchestration

Docker · Podman · containerd · Buildah · Kubernetes (K8s) · k3s · k0s ·
Minikube · kind · OpenShift · Rancher · Nomad · ECS · EKS · GKE · AKS ·
Fargate · Cloud Run · Knative

## Service mesh and networking

Istio · Linkerd · Consul · Cilium · Envoy · Traefik · NGINX · HAProxy ·
CoreDNS · MetalLB · Calico · Flannel · CNI · Gateway API · Ingress ·
mTLS

## Observability and reliability

Prometheus · Grafana · Loki · Tempo · Mimir · Thanos · Cortex · Datadog ·
New Relic · Honeycomb · Splunk · Elastic Stack · ELK · OpenTelemetry ·
Jaeger · Zipkin · PagerDuty · Opsgenie · VictorOps · Sentry · Rollbar ·
Bugsnag · Statuspage

## SRE practices

SLI · SLO · SLA · Error budget · Toil reduction · Incident management ·
Postmortems · Blameless culture · Chaos engineering · Chaos Monkey ·
Gremlin · Litmus · Game days · Runbooks · On-call rotation · DORA
metrics · MTTR · MTTD · Deployment frequency · Change failure rate ·
Lead time for changes

## Build / packaging / artifacts

Make · Bazel · BuildKit · ko · Jib · Nix · NixOS · Artifactory · Nexus ·
Harbor · ECR · GCR · Docker Hub · Sigstore · Cosign · SBOM · SLSA

## Secrets and identity

HashiCorp Vault · AWS Secrets Manager · GCP Secret Manager · Azure Key
Vault · External Secrets Operator · cert-manager · SPIFFE / SPIRE ·
OIDC federation · Workload identity · Just-in-time access

## Configuration management

YAML · TOML · JSON · HCL · Jsonnet · CUE · Dhall · Tanka · Kapitan

## Linux / OS

Linux · systemd · cgroups · namespaces · iptables · nftables · eBPF · BPF ·
strace · perf · sysctl · journalctl · kernel tuning · Bash · POSIX shell

## Compliance and security ops

SOC 2 · ISO 27001 · HIPAA · PCI DSS · FedRAMP · Audit logging · CIS
benchmarks · OpenSCAP · Trivy · Grype · Snyk · Falco · OPA · Open
Policy Agent · Conftest · Gatekeeper · Kyverno

## Cost management (FinOps)

Cost allocation tags · Reserved instances · Savings plans · Spot
instances · Right-sizing · Autoscaling · KEDA · Karpenter · Cluster
Autoscaler · FinOps · Kubecost
