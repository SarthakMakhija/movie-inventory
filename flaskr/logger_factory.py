from __future__ import annotations

from flask import Flask

from flaskr.logging.logging_formatter import LoggingConfiguration


class LoggerFactory:

    __instance: LoggerFactory = None

    def __init__(self, app: Flask):
        self.__logger = app.logger

    @classmethod
    def init(cls, app: Flask):
        LoggingConfiguration.configure()
        cls.__instance = LoggerFactory(app)

    @classmethod
    def instance(cls):
        return cls.__instance

    def logger(self):
        return self.__logger
