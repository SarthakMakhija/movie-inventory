from logging import Logger

from flask import Flask
from flask_restful import Api


class Application:
    def __init__(self, app: Flask):
        self.__api = Api(app)
        self.__logger = app.logger

    @property
    def api(self) -> Api:
        return self.__api

    @property
    def logger(self) -> Logger:
        return self.__logger
