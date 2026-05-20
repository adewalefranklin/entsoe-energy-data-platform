import boto3
from entsoe_e_pipeline.extract import Extractor
from entsoe_e_pipeline.logger import get_logger
from entsoe_e_pipeline.exceptions import LoadError
from datetime import datetime, timezone


class S3Loader:
    def __init__(
        self, aws_access_key_id, aws_secret_access_key, bucket_name, region_name, prefix
    ):

        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
        )
        self.bucket_name = bucket_name
        self.prefix = prefix
        self.logger = get_logger(__name__)

    def s3_uploader(self, data, key):
        self.logger.info(
            f"Uploading data to S3 bucket: {self.bucket_name} with key: {key}"
        )
        try:
            timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
            s3_key = f"{self.prefix}/{key}/{timestamp}.xml"
            self.s3_client.put_object(Bucket=self.bucket_name, Key=s3_key, Body=data)
            self.logger.info(f"Data successfully uploaded to S3 at {s3_key}")
            return s3_key
        except Exception as e:
            self.logger.error(f"Error occurred while uploading data to S3: {e}")
            raise LoadError(f"Failed to upload data to S3: {e}")
