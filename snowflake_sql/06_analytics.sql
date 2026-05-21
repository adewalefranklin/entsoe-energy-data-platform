-- create gold_price_generation_analysis

SELECT
    g.generation_date,
    g.production_name,
    g.total_generation,
    p.avg_price,

    CASE
        WHEN p.avg_price IS NULL THEN 'Missing Price Data'
        ELSE 'Price Available'
    END AS price_data_status

FROM gold_daily_generation g

LEFT JOIN (
    SELECT
        DATE(period_start) AS price_date,
        AVG(price_amount) AS avg_price

    FROM bronze_day_ahead_prices

    GROUP BY 1
) p

ON g.generation_date = p.price_date;




-- Generate a gold table that combines daily generation and day-ahead price data, and includes a column indicating whether price data is available for each generation date. This will allow for analysis of the relationship between generation and prices, as well as identification of any gaps in the price data.

CREATE OR REPLACE TABLE gold_generation_price_analysis AS

SELECT
    g.generation_date,
    g.production_name,
    g.total_generation,
    p.avg_price,

    CASE
        WHEN p.avg_price IS NULL THEN 'Missing Price Data'
        ELSE 'Price Available'
    END AS price_data_status

FROM gold_daily_generation g

LEFT JOIN (
    SELECT
        DATE(period_start) AS price_date,
        AVG(price_amount) AS avg_price

    FROM bronze_day_ahead_prices

    GROUP BY 1
) p

ON g.generation_date = p.price_date;

-- verify data in gold_generation_price_analysis

SELECT *
FROM gold_generation_price_analysis;