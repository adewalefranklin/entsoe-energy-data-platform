--Database and schema setup for entsoe energy data pipeline

CREATE OR REPLACE DATABASE entsoe_energy_db;
CREATE OR REPLACE SCHEMA entsoe_schema;
USE DATABASE entsoe_energy_db;
USE SCHEMA entsoe_schema;

--create file format for parquet files from aws s3

CREATE or REPLACE FILE FORMAT parquet_file
TYPE = PARQUET;