                 ┌──────────────────────┐
                 │    ENTSO-E API       │
                 │ Electricity Market   │
                 └──────────┬───────────┘
                            │
                            │ REST/XML API Calls
                            ▼
                 ┌──────────────────────┐
                 │ Python Extract Layer │
                 │  (Extractor Classes) │
                 └──────────┬───────────┘
                            │
                            │ Raw XML/JSON
                            ▼
                 ┌──────────────────────┐
                 │ AWS S3 Raw Zone      │
                 │ raw/entsoe/...       │
                 └──────────┬───────────┘
                            │
                            │ Spark/Glue Transform
                            ▼
                 ┌──────────────────────┐
                 │ S3 Processed Zone    │
                 │ parquet partitioned  │
                 └──────────┬───────────┘
                            │
                            │ COPY INTO / Snowpipe
                            ▼
                 ┌──────────────────────┐
                 │ Snowflake Raw Layer  │
                 └──────────┬───────────┘
                            │
                            │ dbt Models
                            ▼
          ┌────────────────────────────────┐
          │ Star Schema / Analytics Layer  │
          │ fact_prices                    │
          │ fact_generation                │
          │ dim_country                    │
          │ dim_energy_source              │
          │ dim_datetime                   │
          └──────────┬─────────────────────┘
                     │
                     ▼
             ┌───────────────┐
             │ Power BI      │
             │ Dashboarding  │
             └───────────────┘