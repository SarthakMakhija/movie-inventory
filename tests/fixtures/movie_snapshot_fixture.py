from flaskr.entity import db
from flaskr.entity.movie_snapshot import MovieSnapshot


class MovieSnapshotFixture:

    @staticmethod
    def create_a_movie_snapshot(movie_snapshot: MovieSnapshot):
        db.session.add(movie_snapshot)
        db.session.commit()

    @staticmethod
    def delete_all():
        MovieSnapshot.query.delete()
        db.session.commit()
