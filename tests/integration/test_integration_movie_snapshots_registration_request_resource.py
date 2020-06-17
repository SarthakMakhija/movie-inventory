import unittest
from unittest.mock import patch

from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration
from tests.fixtures.movie_snapshots_fixture import MovieSnapshotsFixture
from tests.fixtures.omdb_movie_response_fixture import mock_omdb_movie_response
from tests.test_client import add_test_client


@application_test()
@add_test_client()
class MovieSnapshotsRegistrationRequestResourceIntegrationTest(unittest.TestCase):

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_register_movie_snapshots_give_movie_titles(self, get_requests_mock):
        movie_titles = '{"titles": ["Jumanji", "3 idiots"]}'

        response = self.test_client.post("/movie-snapshots/registration-request",
                                           data=movie_titles,
                                           content_type="application/json",
                                           headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        snapshot_jumanji = MovieSnapshotsFixture.get_by_title("Jumanji")
        snapshot_3idiots = MovieSnapshotsFixture.get_by_title("3 idiots")

        expected = {'registered_snapshots': [{'id': snapshot_jumanji.id, 'title': 'Jumanji'},
                                             {'id': snapshot_3idiots.id, 'title': '3 idiots'}],
                    'registration_failure_titles': []}

        self.assertEqual(201, response.status_code)
        self.assertEqual(expected, response.json)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_register_movie_snapshots_one_with_failure_give_movie_titles(self, get_requests_mock):
        movie_titles = '{"titles": ["Jumanji", "3 idiots", "movie_which_fails_with_omdb"]}'

        response = self.test_client.post("/movie-snapshots/registration-request",
                                           data=movie_titles,
                                           content_type="application/json",
                                           headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        snapshot_jumanji = MovieSnapshotsFixture.get_by_title("Jumanji")
        snapshot_3idiots = MovieSnapshotsFixture.get_by_title("3 idiots")

        expected = {'registered_snapshots': [{'id': snapshot_jumanji.id, 'title': 'Jumanji'},
                                             {'id': snapshot_3idiots.id, 'title': '3 idiots'}],
                    'registration_failure_titles': ['movie_which_fails_with_omdb']}

        self.assertEqual(201, response.status_code)
        self.assertEqual(expected, response.json)

    def tearDown(self) -> None:
        MovieSnapshotsFixture.delete_all()
