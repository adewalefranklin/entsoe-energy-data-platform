select
    timeseries_id,
    business_type,
    curve_type,

    in_domain_code,
    out_domain_code,

    currency,
    price_unit,

    cast(period_start as timestamp_ntz) as period_start,
    cast(period_end as timestamp_ntz) as period_end,

    cast(period_start as date) as price_date,

    resolution,
    position,

    cast(price_amount as float) as day_ahead_price,

    ingestion_time,
    current_timestamp() as updated_at

from {{ ref('stg_day_ahead_prices') }}

where price_amount is not null