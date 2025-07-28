import logging

import pandas as pd
import requests

from config import Settings


class PokemonExtractor:
    def __init__(self, logger: logging.Logger):
        self.configs = Settings()
        self.logger = logger

    def fetch_pokemon_data(self, limit: int = 100, offset: int = 0) -> list[dict]:
        """
        Fetches a list of Pokémon and their detailed data from the PokeAPI.

        Args:
            limit (int): The number of Pokémon to fetch.
            offset (int): The offset to start fetching from.

        Returns:
            list[dict]: A list of Pokémon and their detailed data.
        """
        url = f"{self.configs.BASE_URL}/pokemon?limit={limit}&offset={offset}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("results", [])

    def _extract_pokemon_id(self, pokemon_url: str) -> int:
        """
        Extracts the Pokémon ID from the URL.

        Args:
            pokemon_url (str): The URL of the Pokémon.

        Returns:
            int: The ID of the Pokémon.
        """
        return int(pokemon_url.split("/")[-2])

    def _fetch_pokemon_details(self, pokemon_id: int) -> dict:
        """
        Fetches the details of a Pokémon from the PokeAPI.

        Args:
            pokemon_id (int): The ID of the Pokémon.

        Returns:
            dict: The details of the Pokémon.
        """
        detail_url = f"{self.configs.BASE_URL}/pokemon/{pokemon_id}"
        self.logger.info(f"Fetching details for Pokemon {pokemon_id}")
        response = requests.get(detail_url)
        response.raise_for_status()
        pokemon_data = response.json()
        return pokemon_data

    def _build_pokemon_dict(self, pokemon_data: dict) -> dict:
        """
        Builds a dictionary of Pokémon data.

        Args:
            pokemon_data (dict): The data of the Pokémon.

        Returns:
            dict: The dictionary of Pokémon data.
        """
        pokemon_dict = {
            "ID": pokemon_data["id"],
            "Name": pokemon_data["name"].title(),  # apply title case
            "Base Experience": pokemon_data["base_experience"],
            "Types": [
                pokemon_type["type"]["name"] for pokemon_type in pokemon_data["types"]
            ],
            "HP": None,
            "Attack": None,
            "Defense": None,
        }
        for pokemon_stat in pokemon_data["stats"]:
            if pokemon_stat["stat"]["name"] == "hp":
                pokemon_dict["HP"] = pokemon_stat["base_stat"]
            elif pokemon_stat["stat"]["name"] == "attack":
                pokemon_dict["Attack"] = pokemon_stat["base_stat"]
            elif pokemon_stat["stat"]["name"] == "defense":
                pokemon_dict["Defense"] = pokemon_stat["base_stat"]

        return pokemon_dict

    def build_pokemons_dataframe(self, pokemons_data: list[dict]) -> pd.DataFrame:
        """
        Builds a DataFrame of Pokémon data.

        Args:
            pokemons_data (list[dict]): The data of the Pokémon.

        Returns:
            pd.DataFrame: The DataFrame of Pokémon data.
        """
        pokemon_list = []
        for pokemon in pokemons_data:
            try:
                pokemon_id = self._extract_pokemon_id(pokemon["url"])
                pokemon_details = self._fetch_pokemon_details(pokemon_id)
                pokemon_dict = self._build_pokemon_dict(pokemon_details)
                pokemon_list.append(pokemon_dict)
            except Exception as e:
                self.logger.error(
                    f"Error fetching details for Pokemon {pokemon['name']}: {e}"
                )
        pokemon_dataframe = pd.DataFrame(pokemon_list)
        return pokemon_dataframe
