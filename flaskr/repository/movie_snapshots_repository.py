from typing import List

from flaskr.entity import db
from flaskr.entity.movie_snapshot import MovieSnapshot


class MovieSnapshotsRepository:

    def get_all(self) -> List[MovieSnapshot]:
        return MovieSnapshot.query.all()

    def save_all(self, snapshots: List[MovieSnapshot]):
        db.session.add_all(snapshots)
        db.session.commit()
        return [snapshot.id for snapshot in snapshots]
