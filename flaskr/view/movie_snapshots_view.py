from __future__ import annotations

from flask_restful import fields

from flaskr.entity.movie_snapshot import MovieSnapshot


class MovieSnapshotsView:
    DISPLAYABLE_FIELDS = {
        "title": fields.String,
        "director": fields.String
    }

    def __init__(self, title: str, director: str):
        self.__title = title
        self.__director = director

    @staticmethod
    def make_from(movie_snapshot: MovieSnapshot) -> MovieSnapshotsView:
        return MovieSnapshotsView(movie_snapshot.title, movie_snapshot.director)

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director
