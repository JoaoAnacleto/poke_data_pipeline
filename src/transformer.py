import logging

import pandas as pd


class DataTransformer:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def categorize_experience(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Categorizing Pokemon experience")
        pokemon_dataframe["Category"] = pokemon_dataframe["Base Experience"].apply(
            lambda x: "Weak" if x < 50 else "Medium" if x < 100 else "Strong"
        )
        return pokemon_dataframe

    def count_pokemon_by_type(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Counting Pokemon by type")
        exploded_df = pokemon_dataframe.explode("Types")
        pokemon_count_by_type = exploded_df["Types"].value_counts().reset_index()
        pokemon_count_by_type.columns = ["Type", "Count"]
        self.logger.info("Type analysis complete.")
        return pokemon_count_by_type

    def calculate_type_statistics(
        self, pokemon_dataframe: pd.DataFrame
    ) -> pd.DataFrame:
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
        return type_statistics

    def find_top_pokemon(self, pokemon_dataframe: pd.DataFrame) -> pd.DataFrame:
        self.logger.info("Finding top Pokemon")
        top_pokemon = pokemon_dataframe.sort_values(
            "Base Experience", ascending=False
        ).head(5)
        self.logger.info("Top Pokemon found.")
        return top_pokemon
