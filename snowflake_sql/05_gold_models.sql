-- create gold table for daily total generation per production type

CREATE OR REPLACE TABLE gold_daily_generation AS

SELECT
    DATE(period_start) AS generation_date,
    production_name,
    SUM(quantity) AS total_generation

FROM silver_actual_generation

GROUP BY 1, 2;

-- verify data in gold_daily_generation

SELECT* 
FROM gold_daily_generation
LIMIT 10
