import json
import unittest
from http import HTTPStatus

import requests_mock

from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration
from tests.fixtures.movie_snapshots_fixture import MovieSnapshotsFixture
from tests.test_client import add_test_client


@application_test()
@add_test_client()
class MovieSnapshotsRegistrationRequestResourceIntegrationTest(unittest.TestCase):

    @requests_mock.Mocker()
    def test_should_register_movie_snapshots_give_movie_titles(self, mock_request):
        movie_titles = '{"titles": ["Jumanji", "3 idiots"]}'

        mock_request.get(f"http://www.omdbapi.com/?t=Jumanji&apikey={TestConfiguration.OMDB_API_KEY}", text=json.dumps(
            {
                "Title": "Jumanji",
                "Director": "",
                "Released": "1 Jan 1970",
                "Ratings": []
            }
        ))

        mock_request.get(f"http://www.omdbapi.com/?t=3 idiots&apikey={TestConfiguration.OMDB_API_KEY}", text=json.dumps(
            {
                "Title": "3 idiots",
                "Director": "",
                "Released": "1 Jan 1970",
                "Ratings": []
            }
        ))

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

    @requests_mock.Mocker()
    def test_should_register_movie_snapshots_one_with_failure_give_movie_titles(self, mock_request):
        movie_titles = '{"titles": ["Jumanji", "movie_which_fails_with_omdb"]}'

        mock_request.get(f"http://www.omdbapi.com/?t=Jumanji&apikey={TestConfiguration.OMDB_API_KEY}", text=json.dumps(
            {
                "Title": "Jumanji",
                "Director": "",
                "Released": "1 Jan 1970",
                "Ratings": []
            }
        ))

        mock_request.get(
            f"http://www.omdbapi.com/?t=movie_which_fails_with_omdb&apikey={TestConfiguration.OMDB_API_KEY}",
            status_code= HTTPStatus.INTERNAL_SERVER_ERROR)

        response = self.test_client.post("/movie-snapshots/registration-request",
                                         data=movie_titles,
                                         content_type="application/json",
                                         headers=[("x-api-key", TestConfiguration.X_API_KEY)])

        snapshot_jumanji = MovieSnapshotsFixture.get_by_title("Jumanji")

        expected = {'registered_snapshots': [{'id': snapshot_jumanji.id, 'title': 'Jumanji'}],
                    'registration_failure_titles': ['movie_which_fails_with_omdb']}

        self.assertEqual(201, response.status_code)
        self.assertEqual(expected, response.json)

    def tearDown(self) -> None:
        MovieSnapshotsFixture.delete_all()
