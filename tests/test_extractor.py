import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logging import Logger
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
import requests

from src.extractor import PokemonExtractor

MOCK_POKEMON_LIST = [
    {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
    {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
]

MOCK_POKEMON_DETAILS = {"id": 25, "name": "pikachu", "base_experience": 112}


@pytest.fixture
def extractor():
    return PokemonExtractor(Logger("test_extractor"))


@patch("requests.get")
def test_fetch_pokemon_data(mock_get, extractor):
    mock_response = MagicMock()
    mock_response.json.return_value = {"results": MOCK_POKEMON_LIST}
    mock_get.return_value = mock_response

    result = extractor.fetch_pokemon_data(limit=2, offset=0)

    assert len(result) == 2
    assert result[0]["name"] == "bulbasaur"
    assert mock_get.call_count == 1
    mock_get.assert_called_with("https://pokeapi.co/api/v2/pokemon?limit=2&offset=0")


def test_extract_pokemon_id(extractor):
    url = "https://pokeapi.co/api/v2/pokemon/25/"
    result = extractor._extract_pokemon_id(url)
    assert result == 25


def test_fetch_pokemon_details(extractor):
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_POKEMON_DETAILS

    with patch("requests.get", return_value=mock_response):
        result = extractor._fetch_pokemon_details(25)

    assert result["name"] == MOCK_POKEMON_DETAILS["name"]
    assert result["base_experience"] == MOCK_POKEMON_DETAILS["base_experience"]


@patch("requests.get")
def test_fetch_pokemon_details_error_handling(mock_get, extractor):
    mock_get.side_effect = requests.exceptions.RequestException("API Error")

    with pytest.raises(requests.exceptions.RequestException):
        extractor._fetch_pokemon_details(25)


@patch("requests.get")
def test_build_pokemons_dataframe_error_handling(mock_get, extractor):
    mock_get.side_effect = requests.exceptions.RequestException("API Error")

    result = extractor.build_pokemons_dataframe(MOCK_POKEMON_LIST)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 0  # Empty dataframe due to errors


@pytest.mark.parametrize(
    "url",
    [
        "https://pokeapi.co/api/v2/pokemon/123/",
        "https://pokeapi.co/api/v2/pokemon/abc/",  # Invalid URL
        "https://pokeapi.co/api/v2/pokemon/",  # Missing ID
    ],
)
def test_extract_pokemon_id_invalid_url(extractor, url):
    if url == "https://pokeapi.co/api/v2/pokemon/123/":
        assert extractor._extract_pokemon_id(url) == 123
    else:
        with pytest.raises(ValueError):
            extractor._extract_pokemon_id(url)


@pytest.mark.parametrize("limit,offset", [(100, 0), (50, 50), (200, 0)])
def test_fetch_pokemon_data_pagination(extractor, limit, offset):
    mock_response = MagicMock()
    mock_response.json.return_value = {"results": MOCK_POKEMON_LIST}

    with patch("requests.get", return_value=mock_response) as mock_get:
        extractor.fetch_pokemon_data(limit, offset)

    expected_url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    mock_get.assert_called_with(expected_url)
