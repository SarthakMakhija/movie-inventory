from __future__ import annotations


class ApplicationConfig:
    __INSTANCE: ApplicationConfig = None

    def __init__(self, config):
        self.__config = config

    @classmethod
    def initialize(cls, config: object):
        cls.__INSTANCE = ApplicationConfig(config)

    @classmethod
    def instance(cls):
        return cls.__INSTANCE

    def get_or_fail(self, key):
        return self.__config[key]
