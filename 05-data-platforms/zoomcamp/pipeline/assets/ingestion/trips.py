import pandas as pd


def materialize():
    # Minimal stub to satisfy validation + pipeline execution.
    # You will replace this with real ingestion logic for the homework steps.
    return pd.DataFrame(
        columns=[
            "vendor_id",
            "pickup_datetime",
            "dropoff_datetime",
            "passenger_count",
            "trip_distance",
            "payment_type",
            "total_amount",
            "extracted_at",
        ]
    )
