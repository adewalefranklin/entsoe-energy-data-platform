-- stg_actual_generation_per_type.sql
select *
from {{ source('entsoe_bronze_layers', 'bronze_actual_generation_per_type') }}