import logging
import logging.config

from src import PokemonExtractor
from src import DataTransformer
from src import DataReporter

logging.config.fileConfig("config/logging.conf")
logger = logging.getLogger(__name__)


def main():
    try:
        extractor = PokemonExtractor(logger)
        pokemons_data = extractor.fetch_pokemon_data(limit=100)
        pokemons_dataframe = extractor.build_pokemons_dataframe(pokemons_data)

        (
            pokemons_dataframe,
            pokemons_by_type_dataframe,
            pokemons_type_statistics_dataframe,
            pokemons_top_5_dataframe,
        ) = DataTransformer(logger).transform_pokemon_data(pokemons_dataframe)

        DataReporter(logger).generate_all_reports(
            pokemons_by_type_dataframe,
            pokemons_top_5_dataframe,
            pokemons_type_statistics_dataframe,
        )

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
