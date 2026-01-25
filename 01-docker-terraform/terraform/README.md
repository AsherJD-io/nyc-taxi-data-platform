# Terraform (Infrastructure as Code)

This module provisions the foundational cloud infrastructure used in the NYC Taxi Data Platform using **Terraform**.

The focus is on:
- Declarative infrastructure
- Reproducibility
- Safe state management
- Clear separation between infrastructure and application logic

---

## What Is Provisioned

Using Terraform, this week provisions:

- Cloud project / account configuration
- Object storage bucket for raw and processed data
- Dataset / warehouse namespace
- IAM roles and permissions required for data ingestion

> No application containers or pipelines are deployed here.
> Terraform is used strictly for **infrastructure provisioning**, not orchestration.

---

## Directory Structure

```text
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── provider.tf
├── terraform.tfvars.example
└── README.md
```
