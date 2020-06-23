import unittest
from datetime import date
from http import HTTPStatus

import requests
import requests_mock
from flask_restful.representations import json

from flaskr.model.response import Response
from flaskr.omdb_movie_client import OmdbMovieClient, Movie
from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration


@application_test()
class OmdbMovieClientTest(unittest.TestCase):

    @requests_mock.Mocker()
    def test_should_return_omdb_movie_response_with_correct_uri_pattern(self, mock_request):
        mock_request.get(f"http://www.omdbapi.com/?t=3 idiots&apikey={TestConfiguration.OMDB_API_KEY}", text=json.dumps(
            {
                "Title": "3 idiots",
                "Director": "",
                "Released": "1 Jan 1970",
                "Ratings": []
            }
        ))

        omdb_movie_client = OmdbMovieClient()

        response = omdb_movie_client.get_movies_response_for(titles=["3 idiots"])

        self.assertIsNotNone(response)

    @requests_mock.Mocker()
    def test_should_return_two_omdb_movie_in_response(self, mock_request):
        mock_request.get(f"http://www.omdbapi.com/?t=3 idiots&apikey={TestConfiguration.OMDB_API_KEY}", text=json.dumps(
            {
                "Title": "3 idiots",
                "Director": "",
                "Released": "1 Jan 1970",
                "Ratings": []
            }
        ))
        mock_request.get(f"http://www.omdbapi.com/?t=Jumanji&apikey={TestConfiguration.OMDB_API_KEY}", text=json.dumps(
            {
                "Title": "3 idiots",
                "Director": "",
                "Released": "1 Jan 1970",
                "Ratings": []
            }
        ))

        omdb_movie_client = OmdbMovieClient()

        response = omdb_movie_client.get_movies_response_for(titles=["3 idiots", "Jumanji"])

        self.assertEqual(2, response.success_count())

    @requests_mock.Mocker()
    def test_should_return_a_movie_response_with_title_given_single_movie_title(self, mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         text=json.dumps({
                             "Title": "3 idiots",
                             "Director": "",
                             "Released": "1 Jan 1970",
                             "Ratings": []}))

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("3 idiots", movie_response.success_at(0).t().title)

    @requests_mock.Mocker()
    def test_should_return_a_movie_response_with_director_given_single_movie_title(self, mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         text=json.dumps({
                             "Title": "3 idiots",
                             "Director": "Rajkumar Hirani",
                             "Released": "1 Jan 1970",
                             "Ratings": []}))

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("Rajkumar Hirani", movie_response.success_at(0).t().director)

    @requests_mock.Mocker()
    def test_should_return_a_movie_response_with_release_date_given_single_movie_title(self, mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         text=json.dumps({
                             "Title": "3 idiots",
                             "Director": "",
                             "Released": "25 Dec 2009",
                             "Ratings": []
                         }))

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual(date(2009, 12, 25), movie_response.success_at(0).t().released_date)

    @requests_mock.Mocker()
    def test_should_return_a_movie_response_with_a_rating_from_internet_given_single_movie_title(self,
                                                                                                 mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         text=json.dumps({
                             "Title": "3 idiots",
                             "Director": "",
                             "Released": "1 Jan 1970",
                             "Ratings": [{"Source": "internet", "Value": ""}]
                         }))

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("internet", movie_response.success_at(0).t().rating_source_at(0))

    @requests_mock.Mocker()
    def test_should_return_a_movie_response_with_a_rating_of_9_on_10_given_single_movie_title(self, mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         text=json.dumps({
                             "Title": "3 idiots",
                             "Director": "",
                             "Released": "1 Jan 1970",
                             "Ratings": [{"Source": "", "Value": "9/10"}]
                         }))

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("9/10", movie_response.success_at(0).t().rating_value_at(0))

    @requests_mock.Mocker()
    def test_should_return_failure_count_given_request_fails_with_timeout(self, mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         exc=requests.exceptions.Timeout)

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual(1, movie_response.failure_count())

    @requests_mock.Mocker()
    def test_should_return_a_failure_given_request_fails_with_internal_server_error(self, mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         status_code=HTTPStatus.INTERNAL_SERVER_ERROR)

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual(1, movie_response.failure_count())

    @requests_mock.Mocker()
    def test_should_return_a_failure_with_movie_title_given_request_fails(self,
                                                                          mock_request):
        omdb_movie_client = OmdbMovieClient()

        mock_request.get(requests_mock.ANY,
                         exc=requests.exceptions.RequestException)

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("3 idiots", movie_response.failure_at(0).e())
