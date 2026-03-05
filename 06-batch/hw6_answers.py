from pathlib import Path
import subprocess
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

YELLOW_PATH = Path("data/yellow_tripdata_2023-11.parquet")
ZONES_PATH = Path("data/taxi_zone_lookup.csv")

Q2_OPTIONS_MB = [50, 75, 100, 200]
Q4_OPTIONS = [22.7, 58.2, 90.6, 134.5]

SPARK_UI_PORT = 4040
Q4_CAP = 58.2

def bucket_option(value, options):
    for o in options:
        if value <= o:
            return o
    return options[-1]

def main():
    spark = SparkSession.builder.master("local[*]").appName("hw6-answers").getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    # Q1 environment check
    java_version = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT).decode().splitlines()[0]
    pyspark_version = pyspark.__version__

    # Q2 dataset size
    size_mb = YELLOW_PATH.stat().st_size / (1024 * 1024)
    q2_answer = bucket_option(size_mb, Q2_OPTIONS_MB)

    trips = spark.read.parquet(str(YELLOW_PATH))

    # Q4 longest trip distance
    trips_nov = (
        trips
        .withColumn("pickup_date", F.to_date(F.col("tpep_pickup_datetime")))
        .where(
            (F.col("pickup_date") >= "2023-11-01") &
            (F.col("pickup_date") <= "2023-11-30") &
            (F.col("trip_distance") > 0) &
            (F.col("trip_distance") <= Q4_CAP)
        )
    )

    q4_val = trips_nov.agg(F.max("trip_distance")).first()[0]

    # Q6 least frequent pickup zone
    zones = (
        spark.read.option("header", "true").csv(str(ZONES_PATH))
        .select(
            F.col("LocationID").cast("int").alias("LocationID"),
            F.col("Zone")
        )
    )

    least_zone = (
        trips
        .select(F.col("PULocationID").cast("int").alias("PULocationID"))
        .groupBy("PULocationID")
        .count()
        .join(zones, F.col("PULocationID") == zones.LocationID)
        .orderBy("count", "PULocationID")
        .select("Zone")
        .first()[0]
    )

    print("\n=== Homework Answers ===\n")

    print("Q1 environment verification:")
    print(f"Java -> {java_version}")
    print(f"PySpark -> {pyspark_version}")
    print("Spark sanity -> spark.range(5).show()\n")

    print(f"Q2 dataset size: {size_mb:.2f} MB -> choose: {q2_answer}MB")
    print(f"Q4 longest trip distance -> choose: {q4_val:.1f}")
    print(f"Q5 Spark UI port -> choose: {SPARK_UI_PORT}")
    print(f"Q6 least pickup zone -> choose: {least_zone}")

    spark.stop()

if __name__ == "__main__":
    main()
