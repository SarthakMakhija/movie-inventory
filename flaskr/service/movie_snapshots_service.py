from typing import List

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.logger_factory import LoggerFactory
from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository


class MovieSnapshotsService:

    def __init__(self):
        self.movie_snapshots_repository = MovieSnapshotsRepository()
        self.logger = LoggerFactory.instance().logger()

    def get_all(self) -> List[MovieSnapshot]:
        movie_snapshots: List[MovieSnapshot] = self.movie_snapshots_repository.get_all()
        self.logger.info(f"Found a total of {len(movie_snapshots)} movie snapshots")
        return movie_snapshots
