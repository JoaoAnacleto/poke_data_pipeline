import requests
import logging
import logging.config
from settings import Settings


configs = Settings()

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def fetch_pokemon_data(limit: int = 100, offset: int = 0) -> list[dict]:
    url = f"{configs.BASE_URL}/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        raise Exception("Failed to fetch Pokemon data")


if __name__ == "__main__":
    pokemon_data = fetch_pokemon_data()
    logger.info(pokemon_data)
    