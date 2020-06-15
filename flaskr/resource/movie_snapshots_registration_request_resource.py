from flask_restful import Resource, reqparse

from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest


def parse_movie_snapshots_registration_request(func):
    def wrapper(*args, **kargs):
        parser = reqparse.RequestParser()
        parser.add_argument("titles", action="append", required=True, location="json")
        args = parser.parse_args()
        return func(*args, MovieSnapshotsRegistrationRequest(args["titles"]))

    return wrapper


class MovieSnapshotsRegistrationRequestResource(Resource):

    @parse_movie_snapshots_registration_request
    def post(self, movie_snapshots_registration_request: MovieSnapshotsRegistrationRequest):
        return "", 201
