import logging

import pandas as pd


class DataTransformer:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def categorize_experience(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Categorizes Pokemon experience.

        Args:
            pokemon_dataframe (pd.DataFrame): The Pokemon data.

        Returns:
            pd.DataFrame: The Pokemon data with experience categorized.
        """
        self.logger.info("Categorizing Pokemon experience")
        pokemon_dataframe["Category"] = pokemon_dataframe["Base Experience"].apply(
            lambda x: "Weak" if x < 50 else "Medium" if x < 100 else "Strong"
        )
        self.logger.info("Pokemon experience categorized.")
        self.logger.info(f"Pokemon experience: \n {pokemon_dataframe}")
        return pokemon_dataframe

    def count_pokemon_by_type(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame:   
        """
        Counts the number of Pokemon by type.

        Args:
            pokemon_dataframe (pd.DataFrame): The Pokemon data.

        Returns:
            pd.DataFrame: The Pokemon count by type.
        """
        self.logger.info("Counting Pokemon by type")
        exploded_df = pokemon_dataframe.explode("Types")
        pokemon_count_by_type = exploded_df["Types"].value_counts().reset_index()
        pokemon_count_by_type.columns = ["Type", "Count"]
        self.logger.info("Type analysis complete.")
        self.logger.info(f"Pokemon count by type: \n {pokemon_count_by_type}")
        return pokemon_count_by_type

    def calculate_type_statistics(
        self, pokemon_dataframe: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Analyzes Pokémon data by type to get counts and average stats.

        Args:
            pokemon_dataframe (pd.DataFrame): The Pokemon data.

        Returns:
            pd.DataFrame: The type statistics.
        """
        self.logger.info("Calculating type statistics")
        exploded_df = pokemon_dataframe.explode("Types")
        type_statistics = (
            exploded_df.groupby("Types")
            .agg(
                {
                    "HP": "mean",
                    "Attack": "mean",
                    "Defense": "mean",
                }
            )
            .reset_index()
        )
        type_statistics = type_statistics.round(2)
        self.logger.info("Type statistics calculation complete.")
        self.logger.info(f"Type statistics: \n {type_statistics}")
        return type_statistics

    def find_top_pokemon(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Finds the top 5 Pokemon by base experience.

        Args:
            pokemon_dataframe (pd.DataFrame): The Pokemon data.

        Returns:
            pd.DataFrame: The top Pokemon.
        """
        self.logger.info("Finding top Pokemon")
        top_pokemon = pokemon_dataframe.sort_values(
            "Base Experience", ascending=False
        ).head(5)
        self.logger.info("Top Pokemon found.")
        self.logger.info(f"Top Pokemon: \n {top_pokemon}")
        return top_pokemon


    def transform_pokemon_data(self, pokemon_dataframe: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        Transforms the Pokemon data.

        Args:
            pokemon_dataframe (pd.DataFrame): The Pokemon data.

        Returns:
            tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]: The transformed Pokemon data.
        """
        self.logger.info("Transforming Pokemon data")
        pokemon_dataframe = self.categorize_experience(pokemon_dataframe)
        pokemons_by_type_dataframe = self.count_pokemon_by_type(pokemon_dataframe)
        pokemons_type_statistics_dataframe = self.calculate_type_statistics(pokemon_dataframe)
        pokemons_top_5_dataframe = self.find_top_pokemon(pokemon_dataframe)
        self.logger.info("Pokemon data transformation complete.")
        return pokemon_dataframe, pokemons_by_type_dataframe, pokemons_type_statistics_dataframe, pokemons_top_5_dataframe