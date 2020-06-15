import unittest
from unittest.mock import patch

from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration
from tests.fixtures.test_client import TestClient


@application_test()
class MovieSnapshotsRegistrationRequestResource(unittest.TestCase):
    __test_client = TestClient.create()

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_Created_given_a_request_to_register_movie_snapshots(self, movie_snapshots_registration_service):

        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value = []

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": ["3 idiots"]}',
                                           content_type="application/json",
                                           headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        self.assertEqual(201, response.status_code)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_Created_given_a_request_to_register_movie_snapshots_with_single_title(self, movie_snapshots_registration_service):

        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value = []
        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": "3 idiots"}',
                                           content_type="application/json",
                                           headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        self.assertEqual(201, response.status_code)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_Bad_Request_given_a_request_to_register_movie_snapshots_without_titles(self, movie_snapshots_registration_service):

        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value = []
        response = self.__test_client.post("/movie-snapshots/registration-request", headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        self.assertEqual(400, response.status_code)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_snapshot_id_given_a_request_to_register_movie_snapshots(self, movie_snapshots_registration_service):

        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value = ["id_001"]

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": "3 idiots"}',
                                           content_type="application/json",
                                           headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        expected = '{"snapshot_ids": ["id_001"]}'
        self.assertEqual(expected, response.json)

    def test_should_return_Unauthorized_given_a_request_to_register_movie_snapshots_without_header(self):

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": ["3 idiots"]}',
                                           content_type="application/json")

        self.assertEqual(401, response.status_code)
