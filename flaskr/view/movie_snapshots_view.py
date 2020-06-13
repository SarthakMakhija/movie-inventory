from __future__ import annotations

from datetime import date
from typing import List

from flask_restful import fields

from flaskr.entity.movie_snapshot import MovieSnapshot, MovieSnapshotRating


class MovieSnapshotRatingsView:
    DISPLAYABLE_FIELDS = {
        "value": fields.String,
        "source": fields.String
    }

    def __init__(self, value: str, source: str):
        self.__value = value
        self.__source = source

    @staticmethod
    def make_from(movie_snapshot_rating: MovieSnapshotRating) -> MovieSnapshotRatingsView:
        return MovieSnapshotRatingsView(movie_snapshot_rating.value, movie_snapshot_rating.source)

    @property
    def value(self):
        return self.__value

    @property
    def source(self):
        return self.__source


class MovieSnapshotsView:
    DISPLAYABLE_FIELDS = {
        "title": fields.String,
        "director": fields.String,
        "release_year": fields.Integer,
        "release_date": fields.String,
        "ratings": fields.Nested(MovieSnapshotRatingsView.DISPLAYABLE_FIELDS)
    }

    def __init__(self, title: str, director: str, release_date: date, ratings: List[MovieSnapshotRatingsView] = []):
        self.__title = title
        self.__director = director
        self.__release_date = release_date.isoformat()
        self.__release_year = release_date.year
        self.__ratings = ratings

    @staticmethod
    def make_from(movie_snapshot: MovieSnapshot) -> MovieSnapshotsView:
        return MovieSnapshotsView(movie_snapshot.title,
                                  movie_snapshot.director,
                                  movie_snapshot.release_date,
                                  [MovieSnapshotRatingsView.make_from(rating) for rating in movie_snapshot.ratings])

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

    @property
    def ratings(self):
        return self.__ratings
