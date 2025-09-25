from typing import Any
from unittest.mock import MagicMock
import pytest

from testtips import WeatherService  # reexport da versão refatorada

@pytest.mark.parametrize(
    "city,expected_temp",
    [("London", 15), ("Berlin", 20), ("Rome", 18)],
)
def test_parametrized_temperatures(city: str, expected_temp: float) -> None:
    # response fake
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"current": {"temp_c": expected_temp}}

    # client fake injetado
    client = MagicMock()
    client.get.return_value = mock_response

    service = WeatherService(client=client, api_key="fake-key")
    assert service.get_temperature(city) == expected_temp


def test_temperature_raises_error() -> None:
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = Exception("API error")

    client = MagicMock()
    client.get.return_value = mock_response

    service = WeatherService(client=client, api_key="fake-key")
    with pytest.raises(Exception):
        service.get_temperature("any")
