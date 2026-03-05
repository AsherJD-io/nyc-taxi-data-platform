# Week 04 – Analytics Engineering (dbt)

This folder contains my Week 4 work for the **DataTalks.Club Data Engineering Zoomcamp (2026 cohort)**.

The focus of this week was **analytics engineering using dbt**, transforming warehouse data into structured analytical models.

---

## Context

After building the warehouse layer in BigQuery during Week 3, this module introduced **analytics engineering with dbt (Data Build Tool)**.

The goal was to structure SQL transformations into maintainable, version-controlled models that can be executed reproducibly.

The emphasis was on:

- Structuring transformations using dbt models
- Organizing transformations into staging and analytical layers
- Defining warehouse sources inside dbt
- Executing transformations through the dbt CLI
- Understanding dbt lineage and dependency graphs
- Validating models using dbt tests

All transformations were executed using **dbt Core with BigQuery as the warehouse backend**.

---

## Environment

Tools used:

- **dbt Core**
- **Google BigQuery**
- Python virtual environment

Typical workflow:

```
dbt run
dbt test
dbt docs generate
dbt docs serve
```

---

## Dataset

The models operate on the **NYC Taxi dataset stored in BigQuery**, produced during the warehouse module.

Primary tables used:

```
ny_taxi.yellow_tripdata
ny_taxi.green_tripdata
ny_taxi.taxi_zone_lookup
```

These tables serve as **sources for dbt transformations**.

---

## Model Structure

The dbt project organizes transformations into layers.

### Staging Models

Staging models normalize the raw warehouse tables.

Examples include:

```
stg_yellow_tripdata
stg_green_tripdata
stg_zones
```

Typical transformations include:

- column renaming
- data type normalization
- removal of unused fields
- preparation for analytical joins

---

### Analytical Models

Analytical models combine staging tables into structures suitable for analysis.

Examples include fact and dimension tables derived from taxi trip data and zone information.

These models form the **analytical layer of the warehouse**.

---

## Homework Verification

Homework queries were executed against the dbt-generated tables inside BigQuery.

Verification steps included:

- Running `dbt run` to build all models
- Executing homework SQL queries against transformed tables
- Validating counts and aggregations
- Inspecting the dbt lineage graph

All transformations executed successfully and produced consistent analytical results.

---

## Key Learnings

- dbt provides a **structured framework for SQL transformations in analytics pipelines**.
- Organizing transformations into **staging and analytical layers** improves clarity and maintainability.
- dbt automatically manages **model dependencies through a DAG**.
- Version-controlled SQL transformations improve **pipeline reproducibility**.
- dbt integrates cleanly with cloud warehouses such as BigQuery.

---

## Repository Structure

```
04-analytics-engineering/
│
├── analyses/
├── macros/
├── models/
├── seeds/
├── snapshots/
├── tests/
│
├── dbt_project.yml
├── .gitignore
└── README.md
```

---

## Notes

This directory contains the **dbt project used to transform warehouse tables into analytics-ready models**.

All transformations are version controlled and reproducible through the dbt CLI.

---

⬅ [Project repository](https://github.com/AsherJD-io/nyc-taxi-data-platform)  
⬅ [Week 03 – Data Warehousing (BigQuery)](https://github.com/AsherJD-io/nyc-taxi-data-platform/tree/main/03-data-warehouse)
