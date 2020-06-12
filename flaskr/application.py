from logging import Logger

from flask import Flask
from flask_restful import Api

from flaskr.logging.logging_formatter import LoggingConfiguration
from flaskr.rest_resource_registry import RestResourceRegistry


class Application:
    def __init__(self, app: Flask):
        LoggingConfiguration.configure()
        self.__app = app
        self.__logger = self.__app.logger
        self.__api = Api(self.__app)
        RestResourceRegistry(self.__api)

    @property
    def api(self) -> Api:
        return self.__api

    @property
    def app(self) -> Flask:
        return self.__app

    @property
    def logger(self) -> Logger:
        return self.__logger
