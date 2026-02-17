with green as (

    select
        'Green' as service_type,
        lpep_pickup_datetime as pickup_datetime,
        lpep_dropoff_datetime as dropoff_datetime,
        pulocationid,
        dolocationid,
        total_amount
    from {{ ref('stg_green_tripdata') }}

),

yellow as (

    select
        'Yellow' as service_type,
        tpep_pickup_datetime as pickup_datetime,
        tpep_dropoff_datetime as dropoff_datetime,
        pulocationid,
        dolocationid,
        total_amount
    from {{ ref('stg_yellow_tripdata') }}

)

select * from green
union all
select * from yellow
