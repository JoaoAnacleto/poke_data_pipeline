import logging
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from config import Settings


class DataReporter:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.configs = Settings()
        self.__clean_reports_directory()

    def __clean_reports_directory(self):
        """
        Cleans the reports directory.
        """
        list_reports = os.listdir(self.configs.OUTPUT_DIR)
        for report in list_reports:
            os.remove(os.path.join(self.configs.OUTPUT_DIR, report))

    def generate_type_distribution_chart(self, pokemon_by_type_dataframe: pd.DataFrame):
        """
        Generates a bar chart of Pokemon distribution by type.

        Args:
            pokemon_by_type_dataframe (pd.DataFrame): The Pokemon data.
        """
        self.logger.info("Building graph bar pokemon by type")
        os.makedirs(self.configs.OUTPUT_DIR, exist_ok=True)
        chart_path = os.path.join(self.configs.OUTPUT_DIR, "graph_pokemon_by_type.png")
        try:
            plt.figure(figsize=(12, 8))
            sns.set_theme(style="whitegrid")
            ax = sns.barplot(
                x="Count",
                y="Type",
                data=pokemon_by_type_dataframe.sort_values("Count", ascending=False),
                palette="viridis",
                hue="Type",
                legend=False,
            )

            ax.set_title("Pokémon Distribution by Type", fontsize=16)
            ax.set_xlabel("Number of Pokémon", fontsize=12)
            ax.set_ylabel("Type", fontsize=12)

            plt.tight_layout()
            plt.savefig(chart_path)
            plt.close()
            self.logger.info(f"Graph saved to {chart_path}")
        except Exception as e:
            self.logger.error(f"Failed to generate graph: {str(e)}")

    def export_top_5_pokemon_csv(self, pokemon_top_5_dataframe: pd.DataFrame):
        """
        Exports the top 5 Pokemon to a CSV file.

        Args:
            pokemon_top_5_dataframe (pd.DataFrame): The Pokemon data.
        """
        self.logger.info("Exporting top 5 pokemon to csv")
        os.makedirs(self.configs.OUTPUT_DIR, exist_ok=True)
        csv_path = os.path.join(self.configs.OUTPUT_DIR, "top_5_pokemon.csv")
        try:
            pokemon_top_5_dataframe.to_csv(csv_path, index=False)
            self.logger.info(f"Top 5 pokemon saved to {csv_path}")
        except Exception as e:
            self.logger.error(f"Failed to export top 5 pokemon: {str(e)}")

    def export_type_statistics_csv(
        self, pokemon_type_statistics_dataframe: pd.DataFrame
    ):
        """
        Exports the type statistics to a CSV file.

        Args:
            pokemon_type_statistics_dataframe (pd.DataFrame): The Pokemon data.
        """
        self.logger.info("Exporting type statistics to csv")
        os.makedirs(self.configs.OUTPUT_DIR, exist_ok=True)
        csv_path = os.path.join(self.configs.OUTPUT_DIR, "type_statistics.csv")
        try:
            pokemon_type_statistics_dataframe.to_csv(csv_path, index=False)
            self.logger.info(f"Type statistics saved to {csv_path}")
        except Exception as e:
            self.logger.error(f"Failed to export type statistics: {str(e)}")

    def _validate_reports_directory(self) -> bool:
        """
        Validates the reports directory.

        Returns:
            bool: True if the reports directory is valid, False otherwise.
        """
        list_expected_reports = [
            "graph_pokemon_by_type.png",
            "top_5_pokemon.csv",
            "type_statistics.csv",
        ]
        list_reports = os.listdir(self.configs.OUTPUT_DIR)
        for report in list_expected_reports:
            if report not in list_reports:
                self.logger.error(f"Report {report} not found")
        return len(list_reports) == len(list_expected_reports)

    def generate_all_reports(
        self,
        pokemon_by_type_dataframe: pd.DataFrame,
        pokemon_top_5_dataframe: pd.DataFrame,
        pokemon_type_statistics_dataframe: pd.DataFrame,
    ) -> bool:
        """
        Generates all reports.

        Args:
            pokemon_by_type_dataframe (pd.DataFrame): The Pokemon data by type.
            pokemon_top_5_dataframe (pd.DataFrame): The Pokemon data top 5.
            pokemon_type_statistics_dataframe (pd.DataFrame): The Pokemon data type statistics.
        """
        self.logger.info("Generating all reports")
        self.generate_type_distribution_chart(pokemon_by_type_dataframe)
        self.export_top_5_pokemon_csv(pokemon_top_5_dataframe)
        self.export_type_statistics_csv(pokemon_type_statistics_dataframe)
        if not self._validate_reports_directory():
            self.logger.error("Reports directory validation failed")
            return False
        self.logger.info("All reports generated successfully")
        return True
