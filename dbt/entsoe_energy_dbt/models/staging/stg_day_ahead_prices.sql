select *
from {{ source('entsoe_bronze_layers', 'bronze_day_ahead_prices') }}