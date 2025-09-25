from typing import Any
from unittest.mock import MagicMock
import pytest

from testtips import WeatherService

@pytest.fixture
def weather_service() -> WeatherService:
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"current": {"temp_c": 25}}

    client = MagicMock()
    client.get.return_value = mock_response

    return WeatherService(client=client, api_key="fake-key")


def test_fixture_usage(weather_service: WeatherService) -> None:
    assert weather_service.get_temperature("Sao Paulo") == 25
