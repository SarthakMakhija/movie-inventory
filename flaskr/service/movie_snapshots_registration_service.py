from typing import List, Dict

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.omdb_movie_client import OmdbMovieClient
from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository


class MovieSnapshotsRegistrationService:

    def __init__(self):
        self.movie_snapshots_repository = MovieSnapshotsRepository()
        self.omdb_client = OmdbMovieClient()

    def register_snapshots_for(self, a_request: MovieSnapshotsRegistrationRequest) -> List[str]:
        movies = self.omdb_client.get_movies_for(a_request.titles)
        snapshots: List[MovieSnapshot] = [movie.to_movie_snapshot() for movie in movies]

        if snapshots:
            return self.movie_snapshots_repository.save_all(snapshots)
        else:
            return []

