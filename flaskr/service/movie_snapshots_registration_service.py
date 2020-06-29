import logging
from typing import List

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.event.movie_snapshot_registered_event import MovieSnapshotRegisteredEvent
from flaskr.model.movie_registration_snapshots_response import MovieSnapshotsRegistrationResponse
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.model.registered_snapshot import RegisteredSnapshot
from flaskr.model.response import Response
from flaskr.omdb_movie_client import OmdbMovieClient, Movie
from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository
from flaskr.service.domain_event_publisher import DomainEventPublisher


class MovieSnapshotsRegistrationService:

    def __init__(self):
        self.movie_snapshots_repository = MovieSnapshotsRepository()
        self.omdb_client = OmdbMovieClient()
        self.domain_event_publisher = DomainEventPublisher()
        self.logger = logging.getLogger(__name__)

    def register_snapshots_for(self,
                               a_request: MovieSnapshotsRegistrationRequest) -> MovieSnapshotsRegistrationResponse:
        movie_response = self.__get_movie_response_for(a_request.titles)
        movies: List[Movie] = movie_response.all_success_t()

        registered_snapshots = self.__register_snapshots_for(movies)

        self.__publish_movie_snapshot_registered_events(registered_snapshots)

        return MovieSnapshotsRegistrationResponse(registered_snapshots, movie_response.all_failure_t())

    def __get_movie_response_for(self, titles):
        movie_response: Response[Movie, str] = self.omdb_client.get_movies_response_for(titles)
        self.logger.info(f"Successfully got a count of {movie_response.success_count()} movies with a "
                         f"failure count of {movie_response.failure_count()}, for a total of "
                         f"{len(titles)} titles")

        return movie_response

    def __register_snapshots_for(self, movies: List[Movie]) -> List[RegisteredSnapshot]:
        snapshots: List[MovieSnapshot] = [movie.to_movie_snapshot() for movie in movies]
        if snapshots:
            return [RegisteredSnapshot.make_from(snapshot)
                    for snapshot in self.movie_snapshots_repository.save_all(snapshots)]
        else:
            return []

    def __publish_movie_snapshot_registered_events(self, registered_snapshots) -> None:
        for registered_snapshot in registered_snapshots:
            self.domain_event_publisher.publish(MovieSnapshotRegisteredEvent(registered_snapshot.snapshot_id))
