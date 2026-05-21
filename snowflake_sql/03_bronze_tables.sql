-- This SQL script creates bronze tables in Snowflake for storing actual generation per type and day-ahead prices from the ENTSOE energy data pipeline. It also includes COPY INTO commands to load data from the respective Snowflake stages and a SELECT statement to preview the loaded data.

CREATE OR REPLACE TABLE bronze_actual_generation_per_type (
    timeseries_id STRING,
    business_type STRING,
    curve_type STRING,
    object_aggregation STRING,
    production_type STRING,
    in_domain_code STRING,
    out_domain_code STRING,
    unit STRING,
    period_start TIMESTAMP_NTZ,
    period_end TIMESTAMP_NTZ,
    resolution STRING,
    position INT,
    quantity FLOAT,
    ingestion_time TIMESTAMP_NTZ
);

-- copy data from the actual generation stage into the bronze table

COPY INTO bronze_actual_generation_per_type
FROM @entsoe_stage
FILE_FORMAT = (TYPE = PARQUET)
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

-- verify data loaded into bronze_actual_generation_per_type

SELECT *
FROM bronze_actual_generation_per_type
LIMIT 20;


--create bronze table for day-ahead prices


CREATE OR REPLACE TABLE bronze_day_ahead_prices (
    TIMESERIES_ID STRING,
    BUSINESS_TYPE STRING,
    CURVE_TYPE STRING,
    IN_DOMAIN_CODE STRING,
    OUT_DOMAIN_CODE STRING,
    CURRENCY STRING,
    PRICE_UNIT STRING,
    PERIOD_START TIMESTAMP,
    PERIOD_END TIMESTAMP,
    RESOLUTION STRING,
    POSITION INTEGER,
    PRICE_AMOUNT FLOAT,
    INGESTION_TIME TIMESTAMP
);

--copy data from day-ahead price stage into bronze_day_ahead_prices table

COPY INTO bronze_day_ahead_prices
FROM @entsoe_price_stage
FILE_FORMAT = parquet_file
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

--verify data loaded into bronze_day_ahead_prices

SELECT* FROM bronze_day_ahead_prices
LIMIT 10
