from __future__ import annotations

from datetime import date

from flaskr.entity.movie_snapshot import MovieSnapshotRating, MovieSnapshot


class MovieSnapshotBuilder:

    def __init__(self, title: str):
        self.__title = title
        self.__director = ""
        self.__release_date = date(1970, 1, 1)
        self.__ratings = []

    @staticmethod
    def snapshot_title(value: str):
        return MovieSnapshotBuilder(title=value)

    def directed_by(self, name: str) -> MovieSnapshotBuilder:
        self.__director = name
        return self

    def released_on(self, a_date: date) -> MovieSnapshotBuilder:
        self.__release_date = a_date
        return self

    def add_rating_with(self, value: str, source: str) -> MovieSnapshotBuilder:
        self.__ratings.append(MovieSnapshotRating(value, source))
        return self

    def finish(self) -> MovieSnapshot:
        return MovieSnapshot(self.__title, self.__director, self.__release_date, self.__ratings)
