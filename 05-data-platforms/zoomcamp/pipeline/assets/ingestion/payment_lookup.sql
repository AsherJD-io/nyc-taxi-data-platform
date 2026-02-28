/* @bruin
name: ingestion.payment_lookup
type: duckdb.sql

materialization:
  type: table
  strategy: create+replace
@bruin */

SELECT * FROM (
  VALUES
    (1, 'credit_card'),
    (2, 'cash'),
    (3, 'no_charge'),
    (4, 'dispute'),
    (5, 'unknown'),
    (6, 'voided_trip')
) AS t(payment_type_id, payment_type_name);
