from os import environ


class Configuration:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    X_API_KEY = environ.get("X_API_KEY")
    OMDB_API_KEY = environ.get("OMDB_API_KEY")
    OMDB_URL = environ.get("OMDB_URL")
