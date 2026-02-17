{{ config(materialized='view') }}

select
    vendorid,
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    passenger_count,
    trip_distance,
    fare_amount,
    total_amount,
    pulocationid,
    dolocationid
from {{ source('ny_taxi', 'green_tripdata') }}
where extract(year from lpep_pickup_datetime) between 2019 and 2020
