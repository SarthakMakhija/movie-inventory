from __future__ import annotations
from typing import Type

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flaskr.configuration import Configuration
from flaskr.logging.logging_formatter import LoggingConfiguration


class Application:

    __INSTANCE: Application = None

    def __init__(self, app):
        self.__app = app
        self.__api = app.api
        self.__config = app.config
        self.__db = app.db

    @classmethod
    def create_app(cls, config: Type[Configuration]) -> Application:
        LoggingConfiguration.configure()
        app = Flask(__name__)
        app.api = Api(app)
        app.config.from_object(config)
        app.db = SQLAlchemy(app)

        cls.__INSTANCE = Application(app)
        return cls.__INSTANCE

    @classmethod
    def instance(cls):
        if cls.__INSTANCE is not None:
            return cls.__INSTANCE
        else:
            return cls.create_app(Configuration)

    @property
    def db(self):
        return self.__db

    @property
    def api(self):
        return self.__api

    @property
    def flask_application(self):
        return self.__app

    def configuration_value_for(self, key):
        return self.__config[key]
