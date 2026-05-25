select
    generation_date,
    production_type,

    sum(generation_mw) as total_generation_mw,

    count(*) as record_count

from {{ ref('silver_actual_generation') }}

group by
    generation_date,
    production_type