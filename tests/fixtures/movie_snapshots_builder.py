from __future__ import annotations

from datetime import date

from flaskr.entity.movie_snapshot import MovieSnapshotRating, MovieSnapshot


class MovieSnapshotsBuilder:

    def __init__(self, title: str):
        self.__title = title
        self.__director = ""
        self.__release_date = date(1970, 1, 1)
        self.__ratings = []
        self.__id = 0

    @staticmethod
    def snapshot_title(value: str):
        return MovieSnapshotsBuilder(title=value)

    @staticmethod
    def any_snapshot():
        return MovieSnapshotsBuilder(title="")

    def snapshot_id(self, snapshot_id: int) -> MovieSnapshotsBuilder:
        self.__id = snapshot_id
        return self

    def directed_by(self, name: str) -> MovieSnapshotsBuilder:
        self.__director = name
        return self

    def released_on(self, a_date: date) -> MovieSnapshotsBuilder:
        self.__release_date = a_date
        return self

    def add_rating_with(self, value: str, source: str) -> MovieSnapshotsBuilder:
        self.__ratings.append(MovieSnapshotRating(value, source))
        return self

    def finish(self) -> MovieSnapshot:
        movie_snapshot = MovieSnapshot(self.__title, self.__director, self.__release_date, self.__ratings)
        movie_snapshot.id = self.__id
        return movie_snapshot
