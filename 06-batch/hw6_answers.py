from pathlib import Path
import shutil
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

YELLOW_PATH = "data/yellow_tripdata_2025-11.parquet"
ZONES_PATH = "data/taxi_zone_lookup.csv"
OUT_PATH = "output/yellow_2025_11_repart4"
SPARK_UI_PORT = 4040

def main():
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("hw6-answers")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    trips = spark.read.parquet(YELLOW_PATH)

    # Q1
    spark_version = spark.version

    # Q2
    out_dir = Path(OUT_PATH)
    if out_dir.exists():
        shutil.rmtree(out_dir)

    trips.repartition(4).write.mode("overwrite").parquet(OUT_PATH)

    parquet_files = sorted(out_dir.glob("*.parquet"))
    sizes_mb = [p.stat().st_size / (1024 * 1024) for p in parquet_files]
    avg_size_mb = sum(sizes_mb) / len(sizes_mb) if sizes_mb else 0.0

    # Q3
    q3_count = (
        trips
        .where(F.to_date("tpep_pickup_datetime") == F.lit("2025-11-15"))
        .count()
    )

    # Q4
    q4_hours = (
        trips
        .where(
            F.col("tpep_pickup_datetime").isNotNull() &
            F.col("tpep_dropoff_datetime").isNotNull() &
            (F.col("tpep_dropoff_datetime") >= F.col("tpep_pickup_datetime"))
        )
        .withColumn(
            "trip_hours",
            (
                F.unix_timestamp("tpep_dropoff_datetime") -
                F.unix_timestamp("tpep_pickup_datetime")
            ) / F.lit(3600.0)
        )
        .agg(F.max("trip_hours").alias("max_trip_hours"))
        .first()["max_trip_hours"]
    )

    # Q6
    zones = (
        spark.read.option("header", "true").csv(ZONES_PATH)
        .select(
            F.col("LocationID").cast("int").alias("LocationID"),
            F.col("Zone")
        )
    )

    least_zone_row = (
        trips
        .select(F.col("PULocationID").cast("int").alias("PULocationID"))
        .where(F.col("PULocationID").isNotNull())
        .groupBy("PULocationID")
        .count()
        .join(zones, F.col("PULocationID") == F.col("LocationID"), "left")
        .orderBy(F.col("count").asc(), F.col("PULocationID").asc())
        .select("Zone", "count", "PULocationID")
        .first()
    )

    print(f"Q1_spark_version: {spark_version}")
    print(f"Q2_avg_parquet_size_mb: {avg_size_mb:.2f}")
    print(f"Q3_trips_started_on_2025_11_15: {q3_count}")
    print(f"Q4_longest_trip_hours: {q4_hours:.2f}")
    print(f"Q5_spark_ui_port: {SPARK_UI_PORT}")
    print(
        "Q6_least_frequent_pickup_zone: "
        f"{least_zone_row['Zone']} "
        f"(LocationID={least_zone_row['PULocationID']}, count={least_zone_row['count']})"
    )

    spark.stop()

if __name__ == "__main__":
    main()
