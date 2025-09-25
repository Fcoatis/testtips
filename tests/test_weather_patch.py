from typing import Any
from unittest.mock import MagicMock
import pytest

from testtips import WeatherService

def test_get_temperature_with_monkeypatch() -> None:
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"current": {"temp_c": 19}}

    client = MagicMock()
    client.get.return_value = mock_response

    service = WeatherService(client=client, api_key="fake-key")
    assert service.get_temperature("Sao Paulo") == 19
