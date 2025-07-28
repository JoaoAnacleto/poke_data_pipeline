from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )
    BASE_URL: str = "https://pokeapi.co/api/v2"
    OUTPUT_DIR: str = "output"
  
    