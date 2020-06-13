from __future__ import annotations

from datetime import date

from flask_restful import fields

from flaskr.entity.movie_snapshot import MovieSnapshot


class MovieSnapshotsView:
    DISPLAYABLE_FIELDS = {
        "title": fields.String,
        "director": fields.String,
        "release_year": fields.Integer,
        "release_date": fields.String
    }

    def __init__(self, title: str, director: str, release_date: date):
        self.__title = title
        self.__director = director
        self.__release_date = release_date.isoformat()
        self.__release_year = release_date.year

    @staticmethod
    def make_from(movie_snapshot: MovieSnapshot) -> MovieSnapshotsView:
        return MovieSnapshotsView(movie_snapshot.title, movie_snapshot.director, movie_snapshot.release_date)

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director

    @property
    def release_date(self):
        return self.__release_date

    @property
    def release_year(self):
        return self.__release_year
