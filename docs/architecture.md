# ENTSO-E Energy Data Platform Architecture

```text
                    ┌──────────────────────────┐
                    │      ENTSO-E API          │
                    │  Generation / Price Data  │
                    └─────────────┬────────────┘
                                  │
                                  │ API Request
                                  ▼
                    ┌──────────────────────────┐
                    │   Python Extract Layer    │
                    │  Extractor + Config       │
                    └─────────────┬────────────┘
                                  │
                                  │ Raw API Response
                                  ▼
                    ┌──────────────────────────┐
                    │      AWS S3 Raw Zone      │
                    │ raw/entsoe/...            │
                    └─────────────┬────────────┘
                                  │
                                  │ Future Step
                                  ▼
                    ┌──────────────────────────┐
                    │ Spark / Glue Transform    │
                    │ Clean + Flatten + Model   │
                    └─────────────┬────────────┘
                                  │
                                  │ Parquet Output
                                  ▼
                    ┌──────────────────────────┐
                    │  AWS S3 Transformed Zone  │
                    │ transformed/entsoe/...    │
                    └─────────────┬────────────┘
                                  │
                                  │ Future Step
                                  ▼
                    ┌──────────────────────────┐
                    │        Snowflake          │
                    │ Staging / Silver / Gold   │
                    └─────────────┬────────────┘
                                  │
                                  │ Future Step
                                  ▼
                    ┌──────────────────────────┐
                    │        Power BI           │
                    │ Energy Analytics Dashboard│
                    └──────────────────────────┘


             ┌──────────────────────────────────────────┐
             │              Apache Airflow               │
             │ DAG Scheduling / Task Execution / Logs     │
             │ CeleryExecutor + Redis + Postgres          │
             └──────────────────────────────────────────┘