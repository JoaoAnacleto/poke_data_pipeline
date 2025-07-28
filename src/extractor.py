import logging
import requests
from settings import Settings
import pandas as pd




class PokemonExtractor:
    def __init__(self, logger: logging.Logger):
        self.configs = Settings()
        self.logger = logger

    def fetch_pokemon_data(self, limit: int = 100, offset: int = 0) -> list[dict]:
        url = f"{self.configs.BASE_URL}/pokemon?limit={limit}&offset={offset}"
        response = requests.get(url)
        if response.status_code == 200:
            self.logger.info("Successfully fetched Pokemon data")
            return response.json().get("results", [])
        else:
            self.logger.error("Failed to fetch Pokemon data")
            raise Exception("Failed to fetch Pokemon data")

    def extract_pokemon_id(self, pokemon_url: str) -> int:
        return int(pokemon_url.split("/")[-2])
        

    def fetch_pokemon_details(self, pokemon_id: int) -> dict:
        detail_url = f"{self.configs.BASE_URL}/pokemon/{pokemon_id}"
        self.logger.info(f"Fetching details for Pokemon {pokemon_id}")
        response = requests.get(detail_url)
        if response.status_code == 200:
            self.logger.info(f"Successfully fetched details for Pokemon {pokemon_id}")
            pokemon_data = response.json()
            return self._build_pokemon_dict(pokemon_data)
        else:
            self.logger.error(f"Failed to fetch details for Pokemon {pokemon_id}")
            raise Exception("Failed to fetch Pokemon details")

    def _build_pokemon_dict(self, pokemon_data: dict) -> dict:
        pokemon_dict = {
            "ID": pokemon_data["id"],
            "Name": pokemon_data["name"],
            "Base Experience": pokemon_data["base_experience"],
            "Types": [pokemon_type["type"]["name"] for pokemon_type in pokemon_data["types"]],
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

    def _build_pokemon_dataframe(self, list_pokemon_dict: list[dict]) -> pd.DataFrame:
        return pd.DataFrame(list_pokemon_dict)
        