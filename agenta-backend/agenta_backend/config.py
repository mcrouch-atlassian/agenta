from pydantic import BaseSettings

import os
import toml
from typing import Optional

# Load the settings from the .toml file
toml_config = toml.load("agenta_backend/config.toml")

# Set the environment variables from the TOML configurations
os.environ["DOCKER_REGISTRY_URL"] = toml_config["docker_registry_url"]
os.environ["REGISTRY"] = toml_config["registry"]
os.environ["DATABASE_URL"] = toml_config["database_url"]
os.environ["DOCKER_HUB_URL"] = toml_config["docker_hub_url"]
os.environ["DATABASE_MODE"] = os.environ.get("DATABASE_MODE", "v2")


class Settings(BaseSettings):
    docker_registry_url: str
    registry: str
    database_url: str
    docker_hub_url: str


settings = Settings()
