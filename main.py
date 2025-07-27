import logging
import logging.config
from src.extractor import PokemonExtractor


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        extractor = PokemonExtractor(logger)
        pokemon_data = extractor.fetch_pokemon_data()
        logger.info(pokemon_data)
    except Exception as e:
        logger.error(e)
