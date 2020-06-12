from typing import List

from flaskr.entity.movie_snapshot import MovieSnapshot


class MovieSnapshotsRepository:
    def get_all(self) -> List[MovieSnapshot]:
        return MovieSnapshot.query.all()
