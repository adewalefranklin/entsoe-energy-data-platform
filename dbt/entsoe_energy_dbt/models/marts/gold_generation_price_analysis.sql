select
    g.generation_date,
    g.production_type,

    g.total_generation_mw,

    avg(p.day_ahead_price) as avg_day_ahead_price,

    case
        when g.total_generation_mw > 0
        then avg(p.day_ahead_price) / g.total_generation_mw
        else null
    end as price_per_mw_indicator

from {{ ref('gold_daily_generation') }} g

left join {{ ref('silver_day_ahead_prices') }} p
    on g.generation_date = p.price_date

group by
    g.generation_date,
    g.production_type,
    g.total_generation_mw