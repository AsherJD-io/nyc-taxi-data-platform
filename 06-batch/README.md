# Week 06 – Batch Processing (Apache Spark)

This folder contains my Week 6 work for the **DataTalks.Club Data Engineering Zoomcamp (2026 cohort)**.

The focus of this week was **batch processing using Apache Spark**, executing distributed transformations on NYC Taxi datasets and validating the homework answers.

---

## Context

This module introduces **distributed batch processing with Apache Spark**.

The objectives were to:

- Run Spark locally using PySpark
- Process Parquet datasets at scale
- Understand Spark partitioning
- Compute aggregations using distributed execution
- Inspect Spark execution through the Spark UI
- Validate analytical results against the homework dataset

All work was executed **locally using PySpark 3.5.0 with OpenJDK 17** inside WSL.

---

## Environment

Environment verification confirmed that Spark was correctly installed.

Components used:

- **OpenJDK 17**
- **PySpark 3.5.0**
- Python virtual environment

Spark sanity test:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()
spark.range(5).show()
```

---

## Dataset

Dataset used for the homework:

```
yellow_tripdata_2025-11.parquet
```

Source:

https://d37ci6vzurychx.cloudfront.net/trip-data/

Supporting lookup table:

```
taxi_zone_lookup.csv
```

Source:

https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv

The dataset was read directly using Spark:

```python
trips = spark.read.parquet("data/yellow_tripdata_2025-11.parquet")
```

Because Parquet is a **self-describing format**, Spark automatically infers the schema from file metadata.

---

## Homework Results

The script `hw6_answers.py` computes the results for Questions **1–6**.

Screenshot of the script output:

![Homework answers](images/hw6_answers.png)

Summary of results:

| Question | Result |
|--------|--------|
| Q1 | PySpark 3.5.0 (Java 17) |
| Q2 | 25MB |
| Q3 | 162,604 |
| Q4 | 90.6 |
| Q5 | 4040 |
| Q6 | Arden Heights |

---

## Repository Structure

```
06-batch/
│
├── data/
│   ├── yellow_tripdata_2025-11.parquet
│   └── taxi_zone_lookup.csv
│
├── images/
│   └── h6_answers.png
│
├── hw6_answers.py
└── README.md
```

---

## Notes

This directory intentionally contains **only the final reproducible script and verification evidence** required to compute the homework answers.

⬅ [Project repository](https://github.com/AsherJD-io/nyc-taxi-data-platform)  
⬅ [Week 05 – Data Platforms (Bruin)](https://github.com/AsherJD-io/nyc-taxi-data-platform/tree/main/05-data-platforms/zoomcamp)
