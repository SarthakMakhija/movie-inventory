from os import environ
from pathlib import Path
from typing import Set

from core.config.configuration import Configuration as CoreConfiguration
from settings import PROJECT_ROOT


class Configuration(CoreConfiguration):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    X_API_KEY = environ.get("X_API_KEY")
    OMDB_API_KEY = environ.get("OMDB_API_KEY")
    OMDB_URL = environ.get("OMDB_URL")
    LOGGING_CONFIG_PATH: Path = Path(f"{PROJECT_ROOT}/logging_config.yaml")
    SERVICE_NAME: str = "movie-inventory-service"
    TRACING_PATCHABLE_LIBRARIES: Set[str] = ["requests"]
