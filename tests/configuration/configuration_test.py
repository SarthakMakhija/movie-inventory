from flaskr.configuration import Configuration


class TestConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = "postgresql://mmaster:mmaster@localhost:5432/movie_snapshots"
    DEBUG = True

