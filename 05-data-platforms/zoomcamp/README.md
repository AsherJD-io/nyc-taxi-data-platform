# Week 05 – Data Platforms (Bruin)

This folder contains my Week 5 work for the **DataTalks.Club Data Engineering Zoomcamp (2026 cohort)**.

The focus of this week was **building a simple data platform using Bruin**, orchestrating SQL-based pipelines executed locally with DuckDB.

---

## Context

After building warehouse models with dbt in Week 4, this module introduced the concept of a **data platform layer**.

The objective was to define structured pipelines that manage:

- ingestion
- transformation
- reporting

The emphasis was on:

- defining SQL pipeline stages
- structuring pipeline execution through configuration
- orchestrating transformations with Bruin
- executing queries using DuckDB
- validating outputs through SQL

All pipelines were executed locally.

---

## Environment

Tools used:

- **Bruin**
- **DuckDB**
- Python virtual environment

Pipeline execution example:

```
bruin run pipeline \
  --env local \
  --config-file .bruin.yml \
  --start-date 2026-02-01 \
  --end-date 2026-02-02
```

---

## Pipeline Design

The pipeline is defined through a configuration file that orchestrates SQL execution.

Bruin manages:

- pipeline dependencies
- SQL execution order
- table creation
- transformation logic

The pipeline produces structured tables from raw datasets into reporting outputs.

---

## Tables Produced

Pipeline execution generates a sequence of datasets representing:

- raw ingestion tables
- intermediate transformation tables
- reporting tables

This represents the full flow from **raw data to analytical output**.

---

## Homework Verification

The homework required executing the pipeline and verifying that the expected tables and outputs were created.

Verification included:

- running the Bruin pipeline
- confirming successful execution
- validating generated tables
- executing SQL queries on the results

All pipeline stages executed successfully.

---

## Key Learnings

- A data platform manages the **full lifecycle of analytical data pipelines**.
- Declarative pipeline configuration simplifies orchestration.
- DuckDB provides a fast analytical execution engine for local pipelines.
- Structured pipeline layers improve maintainability and observability.

---

## Repository Structure

```
05-data-platforms/
│
└── zoomcamp/
    │
    └── pipeline/
        ├── assets/
        ├── pipeline.yml
        ├── pipeline.yml.bak
        ├── .gitignore
        └── README.md
```

---

## Notes

This module demonstrates a **minimal SQL-based data platform**, showing how ingestion, transformation, and reporting pipelines can be orchestrated locally using Bruin.

---

⬅ [Project repository](https://github.com/AsherJD-io/nyc-taxi-data-platform)  
⬅ [Week 04 – Analytics Engineering (dbt)](https://github.com/AsherJD-io/nyc-taxi-data-platform/tree/main/04-analytics-engineering)
