from os import environ
from pathlib import Path
from typing import Set

from ipe_core.config.core_configuration import CoreConfiguration
from settings import PROJECT_ROOT


class Configuration(CoreConfiguration):
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    X_API_KEY = environ.get("X_API_KEY")
    OMDB_API_KEY = environ.get("OMDB_API_KEY")
    OMDB_URL = environ.get("OMDB_URL")
    LOGGING_CONFIG_PATH: Path = Path(f"{PROJECT_ROOT}/logging_config.yaml")
    SERVICE_NAME: str = "movie-inventory-service"
    TRACING_PATCHABLE_LIBRARIES: Set[str] = ["requests"]
    SNS_ENDPOINT_URL = environ.get("SNS_ENDPOINT_URL")
    SNS_TOPIC_NAME = environ.get("SNS_TOPIC_NAME")
    AWS_REGION = environ.get("AWS_REGION")
