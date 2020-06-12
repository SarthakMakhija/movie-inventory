from typing import List

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository


class MovieSnapshotsService:

    def __init__(self):
        self.movie_snapshots_repository = MovieSnapshotsRepository()

    def get_all(self) -> List[MovieSnapshot]:
        return self.movie_snapshots_repository.get_all()
