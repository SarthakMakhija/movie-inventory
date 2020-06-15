import unittest
from unittest.mock import patch

from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration
from tests.fixtures.movie_snapshots_fixture import MovieSnapshotsFixture
from tests.fixtures.omdb_movie_response_fixture import mock_omdb_movie_response
from tests.fixtures.test_client import TestClient


@application_test()
class MovieSnapshotsRegistrationRequestResourceIntegrationTest(unittest.TestCase):
    __test_client = TestClient.create()

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_register_movie_snapshots_give_movie_titles(self, get_requests_mock):
        movie_titles = '{"titles": ["Jumanji", "3 idiots"]}'

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data=movie_titles,
                                           content_type="application/json",
                                           headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        snapshot_ids = MovieSnapshotsFixture.get_all_snapshot_ids()
        expected = '{{"snapshot_ids": {0}}}'.format(snapshot_ids)

        self.assertEqual(201, response.status_code)
        self.assertEqual(expected, response.json)

    def tearDown(self) -> None:
        MovieSnapshotsFixture.delete_all()
