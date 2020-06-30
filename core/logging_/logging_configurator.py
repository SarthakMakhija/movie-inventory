import logging.config
from pathlib import Path

import yaml
from flask import request, has_request_context


class LoggingConfigurator:

    def __init__(self, configuration_file_path: Path):
        if not configuration_file_path.exists() or not configuration_file_path.is_file():
            raise FileNotFoundError(f"File does not exist at path {configuration_file_path}")
        self.__configuration_file_path = configuration_file_path

    def configure(self):
        with self.__configuration_file_path.open() as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)
            LoggingConfigurator.inject_url_in_log_statement()

    @staticmethod
    def inject_url_in_log_statement():
        log_record_factory = logging.getLogRecordFactory()

        def log_record_url_injector(*args, **kwargs):
            record = log_record_factory(*args, **kwargs)
            record.url = request.url if has_request_context() else None
            return record

        logging.setLogRecordFactory(log_record_url_injector)
