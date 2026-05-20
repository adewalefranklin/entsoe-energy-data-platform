from entsoe_e_pipeline.pipeline import EntsoePipeline
from entsoe_e_pipeline.logger import get_logger
from entsoe_e_pipeline.load import S3Loader
from entsoe_e_pipeline.config import Config

logger = get_logger(__name__)


if __name__ == "__main__":
    try:
        config = Config()

        loader = S3Loader(
            aws_access_key_id=config.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=config.get("AWS_SECRET_ACCESS_KEY"),
            bucket_name=config.get("AWS_BUCKET_NAME"),
            region_name=config.get("AWS_REGION"),
            prefix=config.get("PREFIX"),
        )

        pipeline = EntsoePipeline(loader)

        entsoe_endpoints = {
            "actual_generation_per_type": {
                "documentType": "A75",
                "processType": "A16",
            },
            "day_ahead_prices": {
                "documentType": "A44",
            },
            "actual_load": {
                "documentType": "A65",
                "processType": "A16",
            },
            "installed_capacity": {
                "documentType": "A68",
            },
            "cross_border_flows": {
                "documentType": "A11",
            },
        }
        selected_endpoint = "day_ahead_prices"

        base_params = {
            "securityToken": config.get("API_KEY"),
            "in_Domain": "10Y1001A1001A82H",
            "out_Domain": "10Y1001A1001A82H",
            "periodStart": "202605180000",
            "periodEnd": "202605182300",
        }
        params = {
            **entsoe_endpoints[selected_endpoint],
            **base_params,
        }

        s3_key = pipeline.run(selected_endpoint, params)

        logger.info(f"Data successfully processed and stored at: {s3_key}")

    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
