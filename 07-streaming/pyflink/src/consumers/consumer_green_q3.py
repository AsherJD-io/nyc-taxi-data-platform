import json

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "green-trips",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    consumer_timeout_ms=10000,
)

count = 0
total = 0

for message in consumer:
    ride = message.value
    total += 1
    if float(ride["trip_distance"]) > 5.0:
        count += 1

consumer.close()

print(f"total_messages: {total}")
print(f"trip_distance_gt_5: {count}")
