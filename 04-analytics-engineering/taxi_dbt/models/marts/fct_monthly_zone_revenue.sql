{{ config(materialized='table') }}

with trips as (

    select * 
    from {{ ref('int_trips_unioned') }}

),

zones as (

    select *
    from {{ source('ny_taxi', 'taxi_zone_lookup') }}

)

select
    service_type,
    zones.zone,
    extract(year from pickup_datetime) as year,
    extract(month from pickup_datetime) as month,
    sum(total_amount) as total_amount

from trips
join zones
    on trips.pulocationid = zones.locationid

group by 1,2,3,4
