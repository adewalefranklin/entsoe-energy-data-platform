CREATE OR REPLACE DATABASE entsoe_energy_db;
CREATE OR REPLACE SCHEMA enstoe_schema;
USE DATABASE entsoe_energy_db;
USE SCHEMA enstoe_schema;

CREATE or REPLACE FILE FORMAT parquet_file
TYPE = PARQUET;