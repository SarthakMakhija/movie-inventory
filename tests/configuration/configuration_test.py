from flaskr.configuration import Configuration


class TestConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = "postgresql://mmaster:mmaster@localhost:5432/movie_snapshots"
    DEBUG = True
    X_API_KEY = "fake_x_api_key"
    OMDB_API_KEY = "fake_omdb_api_key"
