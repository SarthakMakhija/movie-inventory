from pathlib import Path
from typing import Set


class Configuration:
    LOGGING_CONFIG_PATH: Path = None
    SERVICE_NAME: str = None
    TRACING_PATCHABLE_LIBRARIES: Set[str] = []
