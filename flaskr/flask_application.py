from __future__ import annotations

from typing import Type

from flask import Flask
from flask_restful import Api

from flaskr.configuration import Configuration
from flaskr.entity import db
from flaskr.logger_factory import LoggerFactory
from flaskr.rest_resource_registry import RestResourceRegistry


class Application:

    def __init__(self, config: Type[Configuration]):
        app = Flask(__name__)
        app.config.from_object(config)

        self.__app = app
        self.__api = Api(app)
        self.__config = app.config
        self.__db = db
        self.__logger = app.logger
        db.init_app(app)
        db.app = app

        LoggerFactory.init(app)
        RestResourceRegistry(self.__api)

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
