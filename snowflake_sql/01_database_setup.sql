-- =====================================================
-- DATABASE SETUP
-- This SQL script sets up the Snowflake database and schema for the ENTSOE energy data pipeline. It also creates a file format for Parquet files, which will be used to load data from AWS S3 into Snowflake.
-- =====================================================

--Database and schema setup for entsoe energy data pipeline

CREATE OR REPLACE DATABASE entsoe_energy_db;
CREATE OR REPLACE SCHEMA entsoe_schema;
USE DATABASE entsoe_energy_db;
USE SCHEMA entsoe_schema;

--create file format for parquet files from aws s3

CREATE or REPLACE FILE FORMAT parquet_file
TYPE = PARQUET;