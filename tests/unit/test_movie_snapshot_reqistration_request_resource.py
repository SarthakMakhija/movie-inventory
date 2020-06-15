import unittest
from unittest.mock import patch

from tests.fixtures.test_client import TestClient


class MovieSnapshotsRegistrationRequestResource(unittest.TestCase):
    __test_client = TestClient.create()

    def test_should_return_Created_given_a_request_to_register_movie_snapshots(self):

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": ["3 idiots"]}',
                                           content_type="application/json")

        self.assertEqual(201, response.status_code)

    def test_should_return_Created_given_a_request_to_register_movie_snapshots_with_single_title(self):

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": "3 idiots"}',
                                           content_type="application/json")

        self.assertEqual(201, response.status_code)

    def test_should_return_Bad_Request_given_a_request_to_register_movie_snapshots_without_titles(self):

        response = self.__test_client.post("/movie-snapshots/registration-request")

        self.assertEqual(400, response.status_code)

    @patch("flaskr.resource.movie_snapshots_registration_request_resource.MovieSnapshotsRegistrationService")
    def test_should_return_snapshot_id_given_a_request_to_register_movie_snapshots(self, movie_snapshots_registration_service):
        movie_snapshots_registration_service.return_value.register_snapshots_for.return_value = {"snapshot_ids": ["id_001"]}

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": "3 idiots"}',
                                           content_type="application/json")

        expected = '{"snapshot_ids": ["id_001"]}'
        self.assertEqual(expected, response.json)
