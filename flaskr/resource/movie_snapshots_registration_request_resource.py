from flask_restful import Resource, reqparse

from flaskr.logger_factory import LoggerFactory
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest


def parse_movie_snapshots_registration_request(func):
    def wrapper(*args, **kargs):
        parser = reqparse.RequestParser()
        parser.add_argument("titles", action="append", required=True, location="json")
        payload = parser.parse_args()
        return func(*args, MovieSnapshotsRegistrationRequest(payload["titles"]))

    return wrapper


class MovieSnapshotsRegistrationRequestResource(Resource):

    def __init__(self):
        self.logger = LoggerFactory.instance().logger()

    @parse_movie_snapshots_registration_request
    def post(self, movie_snapshots_registration_request: MovieSnapshotsRegistrationRequest):
        self.logger.info(f"Received a request for registering movie snapshots with titles = {movie_snapshots_registration_request.titles}")
        return "", 201
