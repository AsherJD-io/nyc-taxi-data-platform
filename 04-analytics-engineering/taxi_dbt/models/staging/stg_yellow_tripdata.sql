{{ config(materialized='view') }}

select
    vendorid,
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    passenger_count,
    trip_distance,
    fare_amount,
    total_amount,
    pulocationid,
    dolocationid
from {{ source('ny_taxi', 'yellow_tripdata') }}
