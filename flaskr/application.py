from logging import Logger

from flask import Flask
from flask_restful import Api

from flaskr.logging.logging_formatter import LoggingConfiguration


class Application:
    def __init__(self, app: Flask):
        LoggingConfiguration.configure()
        self.__logger = app.logger
        self.__api = Api(app)

    @property
    def api(self) -> Api:
        return self.__api

    @property
    def logger(self) -> Logger:
        return self.__logger
