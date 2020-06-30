from __future__ import annotations

from typing import Type

from flask import Flask
from flask_restful import Api

from core.config.configuration import Configuration
from core.logging_.logging_configurator import LoggingConfigurator
from core.tracing.xray_tracing_configurator import XrayTracingConfigurator


class Application:
    __INSTANCE: Application = None

    def __init__(self, config: Type[Configuration]):
        app = Flask(__name__)
        app.config.from_object(config)

        self.__app = app
        self.__api = Api(app)
        self.__config = app.config

        config_instance = config()

        LoggingConfigurator(config_instance.LOGGING_CONFIG_PATH).configure()

        XrayTracingConfigurator(app).configure(config_instance.SERVICE_NAME)

    @classmethod
    def init_app(cls, config: Type[Configuration]) -> Application:
        application = Application(config)
        cls.__INSTANCE = application
        return application

    @property
    def api(self):
        return self.__api

    @property
    def flask_application(self):
        return self.__app

    @classmethod
    def instance(cls):
        return cls.__INSTANCE

    def configuration_value_for(self, key):
        return self.__config[key]
