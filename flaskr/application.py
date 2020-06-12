from logging import Logger

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flaskr.configuration import Configuration
from flaskr.logging.logging_formatter import LoggingConfiguration
from flaskr.rest_resource_registry import RestResourceRegistry


class Application:
    def __init__(self):
        LoggingConfiguration.configure()
        app = Flask(__name__)
        self.__app = app
        self.__logger = self.__app.logger
        self.__api = Api(self.__app)
        self.__app.config.from_object(Configuration())
        self.__db = SQLAlchemy(self.__app)
        RestResourceRegistry(self.__api)

    @property
    def api(self) -> Api:
        return self.__api

    @property
    def app(self) -> Flask:
        return self.__app

    @property
    def db(self) -> SQLAlchemy:
        return self.__db

    @property
    def logger(self) -> Logger:
        return self.__logger
