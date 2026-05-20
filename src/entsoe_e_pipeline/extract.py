import requests
from entsoe_e_pipeline.config import Config
from entsoe_e_pipeline.exceptions import ExtractError
from entsoe_e_pipeline.logger import get_logger


class Extractor:
    def __init__(self):
        self.api_key = Config.get("API_KEY")
        self.base_url = Config.get("BASE_URL")
        self.logger = get_logger(__name__)

    def data_extractor(self, endpoint: str, params: dict) -> dict:
        url = self.base_url
        headers = {"Accept": "application/xml"}
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.text
            self.logger.info(f"Data extracted successfully from {endpoint}")
            return data
        except requests.exceptions.RequestException as e:
            self.logger.error(
                f"Error occurred while extracting data from {endpoint}: {e}"
            )
            raise ExtractError(f"Failed to extract data from {endpoint}")
