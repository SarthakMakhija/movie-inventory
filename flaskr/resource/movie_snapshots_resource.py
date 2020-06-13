from typing import List

from flask_restful import Resource, marshal_with

from flaskr.logger_factory import LoggerFactory
from flaskr.service.movie_snapshots_service import MovieSnapshotsService
from flaskr.view.movie_snapshots_view import MovieSnapshotsView


class MovieSnapshotsResource(Resource):

    def __init__(self):
        self.movie_snapshots_service = MovieSnapshotsService()
        self.logger = LoggerFactory.instance().logger()

    @marshal_with(fields=MovieSnapshotsView.DISPLAYABLE_FIELDS)
    def get(self) -> List[MovieSnapshotsView]:
        self.logger.info("Received request for getting all movie snapshots")
        return [
            MovieSnapshotsView.make_from(movie_snapshot) for movie_snapshot in self.movie_snapshots_service.get_all()
        ]
