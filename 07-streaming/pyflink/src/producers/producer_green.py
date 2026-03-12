import json
from time import time

import pandas as pd
from kafka import KafkaProducer

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet"

columns = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "passenger_count",
    "trip_distance",
    "tip_amount",
    "total_amount",
]

df = pd.read_parquet(url, columns=columns)

# convert datetimes to strings
df["lpep_pickup_datetime"] = df["lpep_pickup_datetime"].astype(str)
df["lpep_dropoff_datetime"] = df["lpep_dropoff_datetime"].astype(str)

# replace NaN with None so JSON writes null instead of NaN
df = df.where(pd.notnull(df), None)

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x, allow_nan=False).encode("utf-8"),
)

topic_name = "green-trips"

t0 = time()

for row in df.to_dict(orient="records"):
    producer.send(topic_name, value=row)

producer.flush()

t1 = time()
print(f"took {(t1 - t0):.2f} seconds")
print(f"sent {len(df)} records")
