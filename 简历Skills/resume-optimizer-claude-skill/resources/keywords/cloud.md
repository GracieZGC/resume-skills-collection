# Cloud Keywords

Vocabulary for cloud engineer, cloud architect, and cloud-specialist
resumes. Used in workflow step 9 when the target is cloud-shaped.

**Usage:** add keywords **only when supported by the user's experience**.
See [rewrite-rules.md](../rewrite-rules.md) §7.

For adjacent roles, branch:
- Infra-as-code, K8s, CI/CD operations → [devops.md](./devops.md)
- Services running on the cloud → [backend.md](./backend.md)

This file lists provider-specific services. Pick the file's
provider-relevant subsection that matches the user's experience. Listing
"AWS, Azure, and GCP" without supporting bullets is keyword-stuffing.

---

## Cross-cloud concepts

VPC · Subnet · Routing · NAT · VPN · Direct Connect · ExpressRoute ·
Interconnect · Peering · Transit gateway · IAM · Identity federation ·
SSO · MFA · KMS · HSM · Certificate management · DNS · CDN · Edge
computing · Multi-region · Multi-AZ · Disaster recovery · RPO · RTO ·
Backup · Snapshot · Tagging · Cost allocation · Quotas · Service limits

## AWS — compute / containers

EC2 · Auto Scaling · Spot Instances · Reserved Instances · Savings
Plans · ECS · Fargate · EKS · Lambda · Lambda@Edge · Step Functions ·
Batch · Lightsail · Outposts · Wavelength · Local Zones · App Runner

## AWS — storage / databases

S3 · S3 Glacier · EBS · EFS · FSx · RDS · Aurora · Aurora Serverless ·
DynamoDB · DynamoDB Streams · ElastiCache · Neptune · DocumentDB ·
Timestream · QLDB · Keyspaces · MemoryDB · Redshift · Redshift Serverless

## AWS — networking / edge

VPC · CloudFront · Route 53 · API Gateway · App Mesh · Cloud Map ·
Global Accelerator · ALB · NLB · CLB · PrivateLink · VPC Lattice ·
Transit Gateway

## AWS — data / analytics / ML

Glue · EMR · Kinesis · Kinesis Data Streams · Kinesis Firehose ·
Kinesis Analytics · MSK (Kafka) · Athena · QuickSight · Lake
Formation · SageMaker · Bedrock · Comprehend · Rekognition · Polly ·
Transcribe · Translate · Textract · Forecast · Personalize

## AWS — security / governance

IAM · IAM Identity Center · Cognito · Secrets Manager · Parameter
Store · KMS · CloudHSM · WAF · Shield · Macie · GuardDuty ·
Inspector · Detective · Security Hub · Audit Manager · Config ·
CloudTrail · Control Tower · Organizations · Service Control Policies

## AWS — operations

CloudWatch · CloudWatch Logs · CloudWatch Metrics · CloudWatch
Synthetics · X-Ray · Systems Manager · OpsWorks · CloudFormation · CDK ·
SAM · Amplify · CodePipeline · CodeBuild · CodeDeploy · CodeArtifact

## Azure — compute / containers

Virtual Machines · VM Scale Sets · Azure Functions · Logic Apps · AKS ·
ACI · App Service · Service Fabric · Container Apps · Spring Apps ·
Batch · HPC

## Azure — storage / databases

Blob Storage · Azure Files · Disk Storage · SQL Database · SQL Managed
Instance · Cosmos DB · PostgreSQL Flexible Server · MySQL Flexible
Server · MariaDB · Synapse · Data Lake Storage · Cache for Redis

## Azure — networking / edge

VNet · Application Gateway · Front Door · CDN · Load Balancer · Traffic
Manager · DNS · ExpressRoute · Bastion · Firewall · DDoS Protection ·
Private Link · API Management

## Azure — data / AI

Data Factory · Databricks · Stream Analytics · Event Hubs · Event Grid ·
Service Bus · HDInsight · Cognitive Services · Azure OpenAI · Azure ML ·
Machine Learning Studio · Synapse Analytics · Purview · Data Explorer

## Azure — security / governance

Microsoft Entra ID (Azure AD) · Conditional Access · Key Vault ·
Defender for Cloud · Sentinel · Policy · Blueprints · Management
Groups · RBAC · Privileged Identity Management

## GCP — compute / containers

Compute Engine · Cloud Functions · Cloud Run · GKE · GKE Autopilot ·
App Engine · Cloud Build · Cloud Tasks · Cloud Scheduler ·
Anthos · Workflows · Dataproc

## GCP — storage / databases

Cloud Storage · Persistent Disk · Filestore · Cloud SQL · AlloyDB ·
Spanner · Bigtable · Firestore · Datastore · Memorystore · BigQuery ·
BigQuery ML · Dataproc · Dataflow · Dataform

## GCP — networking / edge

VPC · Cloud Load Balancing · Cloud CDN · Cloud DNS · Cloud
Interconnect · Cloud NAT · Cloud Armor · Network Connectivity Center ·
Service Directory

## GCP — data / AI

Pub/Sub · Dataflow · Dataproc · Composer · BigQuery · Looker · Vertex
AI · Vertex AI Workbench · AutoML · Model Garden · Document AI ·
Vision AI · Speech-to-Text · Text-to-Speech · Translation API · Gemini

## GCP — security / governance

IAM · Identity Platform · Cloud KMS · Cloud HSM · Security Command
Center · Cloud Armor · Secret Manager · Binary Authorization · VPC
Service Controls · Access Context Manager

## Other cloud / cloud-adjacent

Cloudflare · Cloudflare Workers · Cloudflare R2 · Fastly · DigitalOcean ·
Linode · Hetzner · Vercel · Netlify · Heroku · Render · Fly.io · Railway ·
OVH · Oracle Cloud (OCI) · IBM Cloud · Alibaba Cloud
