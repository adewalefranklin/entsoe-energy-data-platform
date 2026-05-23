import pytest
from entsoe_e_pipeline.extract import Extractor
from entsoe_e_pipeline.exceptions import ExtractError
import requests


def test_data_extractor_success(mocker):

    mocker.patch(
        "entsoe_e_pipeline.extract.Config.get",
        side_effect=["fake_api_key", "fake_base_url"],
    )

    fake_response = mocker.Mock()
    fake_response.raise_for_status.return_value = None
    fake_response.text = "<data>test</data>"

    mock_get = mocker.patch(
        "entsoe_e_pipeline.extract.requests.get", return_value=fake_response
    )

    extractor = Extractor()

    result = extractor.data_extractor("test-endpoint", {"param": "value"})

    assert result == "<data>test</data>"

    mock_get.assert_called_once()


def test_data_extractor_failure(mocker):

    mocker.patch(
        "entsoe_e_pipeline.extract.Config.get",
        side_effect=["FAKE_API_KEY", "FAKE_BASE_URL"],
    )

    mock_get = mocker.patch(
        "entsoe_e_pipeline.extract.requests.get",
        side_effect=ExtractError("API call failed"),
    )

    extractor = Extractor()

    with pytest.raises(ExtractError):
        extractor.data_extractor("test-endpoint", {"param": "value"})

    mock_get.assert_called_once()
