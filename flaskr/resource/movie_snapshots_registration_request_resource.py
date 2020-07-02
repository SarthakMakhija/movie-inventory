import logging
from http import HTTPStatus

from flask_restful import Resource, marshal_with
from ipe_core.exception.undeserializable_json_exception import UndeserializableJsonException

from ipe_core.json_.json_deserializer_decorator import deserialize

from flaskr.error_registry import ErrorRegistry
from flaskr.error_response import HTTPErrorResponse
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.security.authentication import authenticate
from flaskr.service.movie_snapshots_registration_service import MovieSnapshotsRegistrationService
from flaskr.view.movie_snapshots_registration_view import MovieSnapshotsRegistrationView


class MovieSnapshotsRegistrationRequestResource(Resource):
    method_decorators = [authenticate]

    ErrorRegistry.register_error(UndeserializableJsonException,
                                 HTTPErrorResponse(status_code=HTTPStatus.BAD_REQUEST, message="titles is mandatory"))

    def __init__(self):
        self.movie_snapshots_registration_service = MovieSnapshotsRegistrationService()
        self.logger = logging.getLogger(__name__)

    @marshal_with(fields=MovieSnapshotsRegistrationView.DISPLAYABLE_FIELDS)
    @deserialize(target=MovieSnapshotsRegistrationRequest)
    def post(self, movie_snapshots_registration_request: MovieSnapshotsRegistrationRequest):
        self.logger.info(
            f"Received a request for registering movie snapshots with titles "
            f"= {movie_snapshots_registration_request.titles}")

        movie_snapshots_registration_response = self \
            .movie_snapshots_registration_service \
            .register_snapshots_for(a_request=movie_snapshots_registration_request)

        return MovieSnapshotsRegistrationView.make_from(movie_snapshots_registration_response), HTTPStatus.CREATED
