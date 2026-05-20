from datetime import datetime, timedelta
from unittest import loader

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from entsoe_e_pipeline.load import S3Loader
from entsoe_e_pipeline.pipeline import EntsoePipeline
from entsoe_e_pipeline.config import Config

default_args = {
    "owner": "adewale",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def run_entsoe_pipeline():
    config = Config()

    loader = S3Loader(
        aws_access_key_id=config.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=config.get("AWS_SECRET_ACCESS_KEY"),
        bucket_name=config.get("AWS_BUCKET_NAME"),
        region_name=config.get("AWS_REGION"),
        prefix=config.get("PREFIX"),
    )

    pipeline = EntsoePipeline(loader)

    endpoint = "generation"
    params = {
        "documentType": "A75",
        "processType": "A16",
        "in_Domain": "10Y1001A1001A83F",
        "periodStart": "202405010000",
        "periodEnd": "202405020000",
    }

    return pipeline.run(endpoint, params)


with DAG(
    dag_id="entsoe_energy_pipeline",
    default_args=default_args,
    description="Orchestrates ENTSO-E API extraction and S3 raw loading",
    start_date=datetime(2026, 5, 20),
    schedule=None,
    catchup=False,
    tags=["entsoe", "energy", "s3"],
) as dag:

    extract_and_load_to_s3 = PythonOperator(
        task_id="extract_and_load_entsoe_data_to_s3",
        python_callable=run_entsoe_pipeline,
    )
