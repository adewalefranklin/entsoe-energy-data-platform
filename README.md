# ENTSO-E Energy Data Platform Architecture

![Pipeline Architecture](docs/entsoe_architecture.png)


# ENTSO-E Energy Data Platform

This project is an end-to-end data engineering pipeline that extracts electricity market data from the ENTSO-E API, stores raw data in AWS S3, and orchestrates the workflow using Apache Airflow.

The project is designed as a portfolio-grade energy data platform and will be extended with Spark/Glue transformations, Snowflake modelling, dbt, and Power BI analytics.

## Project Goals

- Extract energy data from the ENTSO-E Transparency Platform API
- Store raw API responses in AWS S3
- Orchestrate the pipeline with Apache Airflow
- Build a scalable foundation for Spark transformations
- Prepare data for Snowflake, dbt modelling, and Power BI dashboards

## Current Architecture

ENTSO-E API
   ↓
Python Extract Layer
   ↓
AWS S3 Raw Zone
   ↓
Apache Airflow Orchestration

## Planned Architecture

ENTSO-E API
   ↓
Airflow DAG
   ↓
S3 Raw Zone
   ↓
Spark / AWS Glue Transformation
   ↓
S3 Transformed Zone
   ↓
Snowflake
   ↓
dbt Models
   ↓
Power BI Dashboard

## Tech Stack
-Python
-Apache Airflow 3
-Docker
-CeleryExecutor
-Redis
-PostgreSQL
-AWS S3
-Git / GitHub

## Planned additions:
-Apache Spark
-AWS Glue
-Snowflake
-dbt
-Power BI
-CI/CD with GitHub Actions

## Project Structure

entso_e_energy_pipeline/
│
├── dags/
│   └── entsoe_energy_dag.py
│
├── src/
│   └── entsoe_e_pipeline/
│       ├── config.py
│       ├── extract.py
│       ├── load.py
│       ├── pipeline.py
│       ├── logger.py
│       └── exceptions.py
│
├── docs/
│   └── architecture.md
│
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md

# Airflow Orchestration

The pipeline is orchestrated using Apache Airflow with the CeleryExecutor.

Airflow services include:

-Airflow API server
-Airflow scheduler
-Airflow DAG processor
-Airflow worker
-Redis broker
-PostgreSQL metadata database

The DAG currently executes one main task:

-extract_and_load_entsoe_data_to_s3

This task calls the Python pipeline, extracts ENTSO-E data, and uploads the raw response to AWS S3.

## Running the Project

### Start Airflow with Docker Compose:

-docker compose up -d

### Open Airflow UI:

-http://localhost:8080

### Trigger the DAG:

-entsoe_energy_pipeline

## Environment Variables

### Example:

ENTSOE_API_KEY=your_api_key
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=eu-central-1
AWS_BUCKET_NAME=your_bucket_name
PREFIX=raw/entsoe
FERNET_KEY=your_fernet_key

- The .env file is excluded from Git.

## Current Status

Completed:

-Python extraction layer
-S3 loading layer
-Logging and exception handling
-Dockerized Airflow setup
-Airflow DAG registration
-CeleryExecutor configuration
-Successful DAG execution
-GitHub version control

Next steps:

-Add Spark transformation layer
-Write transformed data as Parquet
-Add Snowflake ingestion
-Add dbt models
-Add CI/CD pipeline
-Build Power BI dashboard


