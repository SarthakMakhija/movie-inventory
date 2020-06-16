from typing import List, Dict

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.logger_factory import LoggerFactory
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.model.response import Response
from flaskr.omdb_movie_client import OmdbMovieClient, Movie
from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository


class MovieSnapshotsRegistrationService:

    def __init__(self):
        self.movie_snapshots_repository = MovieSnapshotsRepository()
        self.omdb_client = OmdbMovieClient()
        self.logger = LoggerFactory.instance().logger()

    def register_snapshots_for(self, a_request: MovieSnapshotsRegistrationRequest) -> List[str]:
        movie_response = self.__get_movie_response_for(a_request.titles)
        movies: List[Movie] = movie_response.all_success_t()
        snapshots: List[MovieSnapshot] = [movie.to_movie_snapshot() for movie in movies]

        if snapshots:
            return [snapshot.id for snapshot in self.movie_snapshots_repository.save_all(snapshots)]
        else:
            return []

    def __get_movie_response_for(self, titles):
        movie_response: Response[Movie, str] = self.omdb_client.get_movies_response_for(titles)
        self.logger.info(f"Successfully got a count of {movie_response.success_count()} movies with a "
                         f"failure count of {movie_response.failure_count()}, for a total of "
                         f"{len(titles)} titles")

        return movie_response

