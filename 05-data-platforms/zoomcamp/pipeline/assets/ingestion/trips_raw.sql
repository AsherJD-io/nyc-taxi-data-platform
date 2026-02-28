/* @bruin
name: ingestion.trips_raw
type: duckdb.sql

materialization:
  type: table
  strategy: create+replace
@bruin */

SELECT
  CAST(NULL AS INTEGER)   AS vendor_id,
  CAST(NULL AS TIMESTAMP) AS pickup_datetime,
  CAST(NULL AS TIMESTAMP) AS dropoff_datetime,
  CAST(NULL AS INTEGER)   AS passenger_count,
  CAST(NULL AS DOUBLE)    AS trip_distance,
  CAST(NULL AS INTEGER)   AS payment_type,
  CAST(NULL AS DOUBLE)    AS total_amount,
  CAST(NULL AS TIMESTAMP) AS extracted_at
WHERE 1 = 0;
