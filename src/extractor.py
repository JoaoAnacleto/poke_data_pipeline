import logging
import requests
from settings import Settings




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

    def fetch_pokemon_details(self, pokemon_id: int) -> dict:
        detail_url = f"{self.configs.BASE_URL}/pokemon/{pokemon_id}"
        self.logger.info(f"Fetching details for Pokemon {pokemon_id}")
        response = requests.get(detail_url)
        if response.status_code == 200:
            self.logger.info(f"Successfully fetched details for Pokemon {pokemon_id}")
            return response.json()
        else:
            self.logger.error(f"Failed to fetch details for Pokemon {pokemon_id}")
            raise Exception("Failed to fetch Pokemon details")