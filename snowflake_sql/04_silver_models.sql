-- =====================================================
-- SILVER MODELS
-- Cleaned and enriched datasets, ready for analysis and reporting
-- =====================================================

--create silver tables for actual generation per type with production type names

CREATE OR REPLACE TABLE dim_production_type (
    production_code STRING,
    production_name STRING
);

-- insert production type codes and names into dim_production_type

INSERT INTO dim_production_type VALUES
('B02', 'Brown Coal/Lignite'),
('B03', 'Coal Gas'),
('B04', 'Natural Gas'),
('B05', 'Hard Coal'),
('B06', 'Oil'),
('B09', 'Geothermal'),
('B10', 'Hydro Pumped Storage'),
('B11', 'Hydro Run-of-River'),
('B12', 'Hydro Water Reservoir'),
('B15', 'Other Renewables'),
('B17', 'Waste'),
('B20', 'Other');


-- verify data inserted into dim_production_type

SELECT
    b.*,
    d.production_name

FROM bronze_actual_generation_per_type b
LEFT JOIN dim_production_type d
    ON b.production_type = d.production_code;

    -- create silver table for actual generation per type with production type names

CREATE OR REPLACE TABLE silver_actual_generation AS

SELECT
    b.timeseries_id,
    b.business_type,
    b.curve_type,
    b.object_aggregation,
    b.production_type,
    d.production_name,
    b.in_domain_code,
    b.out_domain_code,
    b.unit,
    b.period_start,
    b.period_end,
    b.resolution,
    b.position,
    b.quantity,
    b.ingestion_time

FROM bronze_actual_generation_per_type b

LEFT JOIN dim_production_type d
    ON b.production_type = d.production_code;

-- verify data in silver_actual_generation

    SELECT* FROM silver_actual_generation
    LIMIT 10
