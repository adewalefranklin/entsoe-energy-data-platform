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

COPY INTO bronze_actual_generation_per_type
FROM @entsoe_stage
FILE_FORMAT = (TYPE = PARQUET)
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

SELECT *
FROM bronze_actual_generation_per_type
LIMIT 20;


--ENTSOE Day Ahead Prices


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

COPY INTO bronze_day_ahead_prices
FROM @entsoe_price_stage
FILE_FORMAT = parquet_file
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

SELECT* FROM bronze_day_ahead_prices
LIMIT 10
