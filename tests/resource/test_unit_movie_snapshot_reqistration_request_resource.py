import unittest
from http import HTTPStatus
from unittest.mock import patch

from flaskr.model.movie_registration_snapshots_response import MovieSnapshotsRegistrationResponse
from flaskr.model.registered_snapshot import RegisteredSnapshot
from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration
from tests.test_client import add_test_client


def empty_movie_snapshot_registration_response():
    return MovieSnapshotsRegistrationResponse([], [])


@application_test()
@add_test_client()
class MovieSnapshotsRegistrationRequestResource(unittest.TestCase):

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_Created_given_a_request_to_register_movie_snapshots(self,
                                                                               movie_snapshots_registration_service):
        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value \
            = empty_movie_snapshot_registration_response()

        response = self.test_client.post("/movie-snapshots/registration-request",
                                         json={"titles": ["3 idiots"]},
                                         headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        self.assertEqual(HTTPStatus.CREATED, response.status_code)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_Created_given_a_request_to_register_movie_snapshots_with_single_title(self,
                                                                                                 movie_snapshots_registration_service):
        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value \
            = empty_movie_snapshot_registration_response()

        response = self.test_client.post("/movie-snapshots/registration-request",
                                         json={"titles": "3 idiots"},
                                         headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        self.assertEqual(HTTPStatus.CREATED, response.status_code)

    @unittest.skip("failing for type error. need to add support in library")
    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_Bad_Request_given_a_request_to_register_movie_snapshots_without_titles(self,
                                                                                                  movie_snapshots_registration_service):
        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value \
            = empty_movie_snapshot_registration_response()

        response = self.test_client.post("/movie-snapshots/registration-request",
                                         headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        self.assertEqual(HTTPStatus.BAD_REQUEST, response.status_code)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_movie_snapshot_registration_view_given_a_request_to_register_movie_snapshots(self,
                                                                                                        movie_snapshots_registration_service):
        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value \
            = MovieSnapshotsRegistrationResponse(registered_snapshots=[RegisteredSnapshot(120, "3 idiots")])

        response = self.test_client.post("/movie-snapshots/registration-request",
                                         json={"titles": "3 idiots"},
                                         headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        expected = {'registered_snapshots': [{'id': 120, 'title': '3 idiots'}], 'registration_failure_titles': []}
        self.assertEqual(expected, response.json)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_movie_snapshot_registration_view_with_failures_given_a_request_to_register_movie_snapshots(
            self,
            movie_snapshots_registration_service):
        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value \
            = MovieSnapshotsRegistrationResponse(registered_snapshots=[], registration_failure_titles=["3 idiots"])

        response = self.test_client.post("/movie-snapshots/registration-request",
                                         json={"titles": "3 idiots"},
                                         headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        expected = {'registered_snapshots': [], 'registration_failure_titles': ["3 idiots"]}
        self.assertEqual(expected, response.json)

    def test_should_return_Unauthorized_given_a_request_to_register_movie_snapshots_without_header(self):
        response = self.test_client.post("/movie-snapshots/registration-request",
                                         json={"titles": ["3 idiots"]})

        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_http_status_INTERNAL_SERVER_ERROR_in_case_of_any_exeption(self,
                                                                                     movie_snapshots_registration_service):
        movie_snapshots_registration_service.return_value.register_snapshots_for.side_effect = Exception('Test')

        response = self.test_client.post("/movie-snapshots/registration-request",
                                         json={"titles": "3 idiots"},
                                         headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        self.assertEqual(500, response.status_code)
