import os
import logging.config
import yaml

from settings import PROJECT_ROOT


class LoggingConfigurator:

    def configure(self):
        default_configuration_file_name = 'logging_config.yaml'

        if self.__file_exists_with(file_name=default_configuration_file_name):
            self.__configure_logger_from_file_with(file_name=default_configuration_file_name)
        else:
            self.__configure_with_default_configuration()

    def __file_exists_with(self, file_name: str):
        config_file_path = os.path.join(PROJECT_ROOT, file_name)
        return os.path.exists(config_file_path)

    def __configure_logger_from_file_with(self, file_name: str):
        config_path = os.path.join(PROJECT_ROOT, file_name)

        with open(config_path) as file:
            config = yaml.safe_load(file.read())
            logging.config.dictConfig(config)

    def __configure_with_default_configuration(self):
        default_logging_level = logging.INFO
        logging.basicConfig(level=default_logging_level)