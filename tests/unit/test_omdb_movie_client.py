import unittest
from datetime import date
from unittest.mock import patch, call, Mock

import requests
from requests import Timeout

from flaskr.model.response import Response
from flaskr.omdb_movie_client import OmdbMovieClient, Movie
from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration
from tests.fixtures.omdb_movie_response_fixture import mock_omdb_movie_response


@application_test()
class OmdbMovieClientTest(unittest.TestCase):

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_fetch_single_movie_response_given_single_movie_title(self,
                                                                         get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        omdb_movie_client.get_movies_response_for(titles=["3 idiots"])
        get_requests_mock.assert_called_once_with(
            f"http://www.omdbapi.com/?t=3 idiots&apikey={TestConfiguration.OMDB_API_KEY}")

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_fetch_multiple_movie_responses_given_multiple_movie_titles(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        omdb_movie_client.get_movies_response_for(["3 idiots", "Jumanji"])

        get_requests_mock.assert_has_calls(
            [call(f"http://www.omdbapi.com/?t=3 idiots&apikey={TestConfiguration.OMDB_API_KEY}"),
             call(f"http://www.omdbapi.com/?t=Jumanji&apikey={TestConfiguration.OMDB_API_KEY}")],
            any_order=False)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_return_a_movie_response_with_title_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("3 idiots", movie_response.success_at(0).t().title)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_return_a_movie_response_with_director_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("Rajkumar Hirani", movie_response.success_at(0).t().director)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_return_a_movie_response_with_release_date_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual(date(2009, 12, 25), movie_response.success_at(0).t().released_date)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_return_a_movie_response_with_a_rating_from_internet_given_single_movie_title(self,
                                                                                                 get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("internet", movie_response.success_at(0).t().rating_source_at(0))

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_omdb_movie_response)
    def test_should_return_a_movie_response_with_a_rating_of_9_on_10_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("9/10", movie_response.success_at(0).t().rating_value_at(0))

    @patch("flaskr.omdb_movie_client.requests.get")
    def test_should_return_a_failure_given_request_fails_with_timeout(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()
        get_requests_mock.side_effect = Timeout

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual(1, movie_response.failure_count())

    @patch("flaskr.omdb_movie_client.requests.get")
    def test_should_a_failure_given_request_fails_with_internal_server_error(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        def mock_response(url):
            response_mock = Mock()
            response_mock.status_code = 500
            response_mock.raise_for_status.side_effect = requests.exceptions.HTTPError
            return response_mock

        get_requests_mock.side_effect = mock_response

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual(1, movie_response.failure_count())

    @patch("flaskr.omdb_movie_client.requests.get")
    def test_should_return_a_failure_with_movie_title_given_request_fails_Timeout(self,
                                                                                  get_requests_mock):
        omdb_movie_client = OmdbMovieClient()
        get_requests_mock.side_effect = Timeout

        movie_response: Response[Movie, str] = omdb_movie_client.get_movies_response_for(["3 idiots"])

        self.assertEqual("3 idiots", movie_response.failure_at(0).e())
