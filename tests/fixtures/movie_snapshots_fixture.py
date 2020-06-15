from typing import List

from flaskr.entity import db
from flaskr.entity.movie_snapshot import MovieSnapshot, MovieSnapshotRating


class MovieSnapshotsFixture:

    @staticmethod
    def create_a_movie_snapshot(movie_snapshot: MovieSnapshot):
        db.session.add(movie_snapshot)
        db.session.commit()

    @staticmethod
    def get_all_snapshot_ids() -> List[MovieSnapshot]:
        return [snapshot.id for snapshot in MovieSnapshot.query.all()]

    @staticmethod
    def delete_all():
        MovieSnapshotRating.query.delete()
        MovieSnapshot.query.delete()
        db.session.commit()
