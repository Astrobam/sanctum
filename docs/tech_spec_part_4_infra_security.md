# Sanctum Tech Spec Part 4: Infrastructure, Deployment & Security

## 1. The Vision: The Foundation and Fortress

This document outlines the operational bedrock of Sanctum. It is the invisible architecture—the foundation and fortress—that ensures the sanctuary is always available, performs flawlessly under pressure, and is impenetrable to threats. Our users trust us with their most private professional aspirations; this infrastructure is our commitment to honoring that trust. We will achieve this through a modern, cloud-native approach that automates deployment, prioritizes security, and scales on demand.

---
## 2. Core Principles

- **Security by Default:** The system is architected to be secure at every layer, from the network to the application code. We assume a zero-trust environment.
- **Infrastructure as Code (IaC):** All cloud resources will be defined declaratively using a tool like Terraform. This ensures our infrastructure is reproducible, version-controlled, and auditable.
- **Automate Everything:** All testing and deployment processes will be fully automated via a CI/CD pipeline to eliminate human error and accelerate development.
- **Leverage Managed Services:** We will use managed cloud services for databases, container orchestration, and other commodity components to reduce operational overhead and focus on building our core product.

---
## 3. User Stories

- **Security:** As a user, I want full confidence that my private conversations and personal data are protected from unauthorized access.
- **Reliability:** As a user, I want the application to be available 24/7 and perform quickly, especially when I need it most.
- **Development:** As a developer, I want to deploy updates to the application safely and automatically, so I can deliver improvements to users without risking downtime.

---
## 4. Cloud Infrastructure

Our infrastructure is designed as a set of containerized services running on a major cloud provider (e.g., AWS), leveraging managed services for data persistence and security.

### Cloud Infrastructure Diagram

This diagram provides a visual overview of our core cloud components and how they interact.

[View Cloud Infrastructure Diagram](diagram/cloud_infrastructure.md)

---
## 5. Deployment Pipeline (CI/CD)

Continuous Integration and Continuous Deployment (CI/CD) are essential for rapid, reliable development. We will use GitHub Actions as our automation server.

### CI/CD Pipeline Diagram

This flowchart illustrates our automated deployment process for the backend and AI Core. A similar, simpler process will be used for the frontend via Vercel.

[View CI/CD Pipeline Diagram](diagram/cicd_pipeline.md)

### Key Stages

1.  **Commit:** A developer pushes code to the `main` branch on GitHub.
2.  **Test:** GitHub Actions automatically runs a suite of tests (linting, unit tests, integration tests).
3.  **Build:** If tests pass, a new, versioned Docker image is built.
4.  **Push:** The image is pushed to a secure container registry (e.g., AWS ECR).
5.  **Deploy:** The deployment command is triggered, which instructs our container orchestrator (e.g., AWS Fargate) to perform a rolling update, replacing the old containers with the new ones with zero downtime.

---
## 6. Security Architecture: The Fortress

Security is woven into the fabric of our design.

- **Data Encryption:**
    - **In Transit:** All network traffic between all services and to the end-user is encrypted using **TLS 1.2+**.
    - **At Rest:** All data stored in our managed databases (PostgreSQL and the Vector DB) is encrypted on disk using **AES-256** by default.
- **Secrets Management:**
    - No secrets (API keys, database credentials, JWT signing keys) will ever be stored in the Git repository.
    - We will use a dedicated secrets manager (e.g., **AWS Secrets Manager**). The application will securely fetch these secrets at runtime.
- **Network Security:**
    - Our services will run within an isolated **Virtual Private Cloud (VPC)**.
    - **Security Groups** (firewalls) will restrict traffic between services, ensuring that, for example, only the backend container can access the user database.
