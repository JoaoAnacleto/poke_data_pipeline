import logging
import logging.config
from src.extractor import PokemonExtractor


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        extractor = PokemonExtractor(logger)
        pokemons_data = extractor.fetch_pokemon_data(limit=10)
        for pokemon in pokemons_data:
            pokemon_id = extractor.extract_pokemon_id(pokemon["url"])
            pokemon_details = extractor.fetch_pokemon_details(pokemon_id)
            logger.info(pokemon_details)
    except Exception as e:
        logger.error(e)
