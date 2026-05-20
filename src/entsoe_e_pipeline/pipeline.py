from entsoe_e_pipeline.logger import get_logger
from entsoe_e_pipeline.exceptions import PipelineError
from entsoe_e_pipeline.extract import Extractor
from entsoe_e_pipeline.load import S3Loader


class EntsoePipeline:

    def __init__(self, loader):

        self.logger = get_logger(__name__)

        self.loader = loader

        self.extractor = Extractor()

    def run(self, entsoe_endpoints, params):

        try:
            self.logger.info(f"Starting pipeline for endpoint: {entsoe_endpoints}")

            data = self.extractor.data_extractor(entsoe_endpoints, params)

            key = f"{entsoe_endpoints.replace('/', '_')}"

            s3_key = self.loader.s3_uploader(data, key)

            self.logger.info(
                f"Pipeline completed successfully. " f"Data stored at: {s3_key}"
            )

            return s3_key

        except Exception as e:

            self.logger.error(f"Pipeline failed: {e}")

            raise PipelineError(f"Pipeline execution failed: {e}")
