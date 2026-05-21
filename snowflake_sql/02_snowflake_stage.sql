-- =====================================================
-- SNOWFLAKE STAGE CREATION
-- Stages are Snowflake objects that point to external locations (like S3 buckets) where data files are stored. They allow Snowflake to access and load data from these locations into Snowflake tables.
-- =====================================================

--create snowflake storage integration for s3 bucket

CREATE OR REPLACE STORAGE INTEGRATION s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 'S3'
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::972775291781:role/snowflake-weather-role'
STORAGE_ALLOWED_LOCATIONS = (
's3://entsoe-energy-bucket/curated/actual_generation_per_type/',
's3://entsoe-energy-bucket/curated/day_ahead_prices/'
);
DESC INTEGRATION s3_int;


--create energy generation stage 

CREATE OR REPLACE STAGE entsoe_stage
URL = 's3://entsoe-energy-bucket/curated/actual_generation_per_type/'
STORAGE_INTEGRATION = s3_int
FILE_FORMAT = parquet_file

LS @entsoe_stage

--create day ahead price stage

CREATE OR REPLACE STAGE entsoe_price_stage
URL = 's3://entsoe-energy-bucket/curated/day_ahead_prices/'
STORAGE_INTEGRATION = s3_int
FILE_FORMAT = parquet_file;

LS @entsoe_price_stage

