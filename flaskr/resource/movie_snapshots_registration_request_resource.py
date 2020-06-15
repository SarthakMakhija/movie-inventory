import json

from flask_restful import Resource, reqparse

from flaskr.logger_factory import LoggerFactory
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.security.authentication import authenticate
from flaskr.service.movie_snapshots_registration_service import MovieSnapshotsRegistrationService


def parse_movie_snapshots_registration_request(func):
    def wrapper(*args, **kargs):
        parser = reqparse.RequestParser()
        parser.add_argument("titles", action="append", required=True, location="json")
        payload = parser.parse_args()
        return func(*args, MovieSnapshotsRegistrationRequest(payload["titles"]))

    return wrapper


class MovieSnapshotsRegistrationRequestResource(Resource):
    method_decorators = [authenticate]

    def __init__(self):
        self.movie_snapshots_registration_service = MovieSnapshotsRegistrationService()
        self.logger = LoggerFactory.instance().logger()

    @parse_movie_snapshots_registration_request
    def post(self, movie_snapshots_registration_request: MovieSnapshotsRegistrationRequest):
        self.logger.info(
            f"Received a request for registering movie snapshots with titles = {movie_snapshots_registration_request.titles}")

        snapshot_ids = self \
            .movie_snapshots_registration_service \
            .register_snapshots_for(a_request=movie_snapshots_registration_request)

        response = {"snapshot_ids": snapshot_ids}
        return json.dumps(response), 201
