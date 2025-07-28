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
        pokemons_data = extractor.fetch_pokemon_data(limit=20)
        pokemons_dataframe = extractor.build_pokemons_dataframe(pokemons_data)
        logger.info(f"Pokemon dataframe: \n {pokemons_dataframe}")

        transformer = DataTransformer(logger)
        pokemons_dataframe = transformer.categorize_experience(pokemons_dataframe)
        logger.info(f"Categorized Pokemon experience: \n {pokemons_dataframe}")

        pokemons_by_type_dataframe = transformer.count_pokemon_by_type(pokemons_dataframe)
        logger.info(f"Pokemon count by type: \n {pokemons_by_type_dataframe}")

        pokemons_type_statistics_dataframe = transformer.calculate_type_statistics(pokemons_dataframe)
        logger.info(f"Pokemon type statistics: \n {pokemons_type_statistics_dataframe}")

        pokemons_top_5_dataframe = transformer.find_top_pokemon(pokemons_dataframe)
        logger.info(f"Top 5 Pokemon: \n {pokemons_top_5_dataframe}")

        reporter = DataReporter(logger)
        reporter.generate_all_reports(pokemons_by_type_dataframe, pokemons_top_5_dataframe, pokemons_type_statistics_dataframe)

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
    