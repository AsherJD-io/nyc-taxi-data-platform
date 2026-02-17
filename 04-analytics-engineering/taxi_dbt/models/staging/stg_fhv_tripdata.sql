select
    dispatching_base_num,
    pickup_datetime,
    dropOff_datetime,
    pulocationid,
    dolocationid,
    sr_flag,
    affiliated_base_number
from {{ source('ny_taxi', 'fhv_tripdata') }}
where dispatching_base_num is not null
