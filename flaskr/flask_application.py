from __future__ import annotations

from typing import Type

from flask import Flask
from flask_restful import Api

from flaskr.configuration import Configuration
from flaskr.entity import db
from flaskr.logging.logging_configurator import LoggingConfigurator
from flaskr.rest_resource_registry import RestResourceRegistry


class Application:

    @staticmethod
    def create_app(config: Type[Configuration]):
        app = Flask(__name__)

        app.config.from_object(config)

        LoggingConfigurator().configure()

        api = Api(app)

        db.init_app(app)

        RestResourceRegistry(api)

        return app
