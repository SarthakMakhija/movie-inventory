import unittest
from datetime import date
from unittest.mock import patch, call

from flaskr.omdb_movie_client import OmdbMovieClient


def mock_movie_response(*args, **kargs):
    class MockResponse:
        def __init__(self, payload, status_code):
            self.json_data = payload
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "http://www.omdbapi.com/?t=3 idiots":
        return MockResponse({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]},
            200
        )
    elif args[0] == "http://www.omdbapi.com/?t=Jumanji":
        return MockResponse({
            "Title": "Jumanji",
            "Director": "Joe Johnston ",
            "Released": "4 Dec 2019",
            "Ratings": []},
            200
        )
    else:
        return {}


class OmdbMovieClientTest(unittest.TestCase):

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_movie_response)
    def test_should_fetch_single_movie_given_single_movie_title(self,
                                                                get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        omdb_movie_client.get_movies_for(titles=["3 idiots"])
        get_requests_mock.assert_called_once_with("http://www.omdbapi.com/?t=3 idiots")

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_movie_response)
    def test_should_fetch_multiple_movies_given_multiple_movie_titles(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        omdb_movie_client.get_movies_for(["3 idiots", "Jumanji"])

        get_requests_mock.assert_has_calls([call("http://www.omdbapi.com/?t=3 idiots"),
                                            call("http://www.omdbapi.com/?t=Jumanji")],
                                           any_order=False)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_movie_response)
    def test_should_return_a_movie_with_title_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movies = omdb_movie_client.get_movies_for(["3 idiots"])

        self.assertEqual("3 idiots", movies[0].title)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_movie_response)
    def test_should_return_a_movie_with_director_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movies = omdb_movie_client.get_movies_for(["3 idiots"])

        self.assertEqual("Rajkumar Hirani", movies[0].director)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_movie_response)
    def test_should_return_a_movie_with_release_date_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movies = omdb_movie_client.get_movies_for(["3 idiots"])

        self.assertEqual(date(2009, 12, 25), movies[0].released_date)

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_movie_response)
    def test_should_return_a_movie_with_a_rating_from_internet_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movies = omdb_movie_client.get_movies_for(["3 idiots"])

        self.assertEqual("internet", movies[0].rating_source_at(0))

    @patch("flaskr.omdb_movie_client.requests.get", side_effect=mock_movie_response)
    def test_should_return_a_movie_with_a_rating_of_9_on_10_given_single_movie_title(self, get_requests_mock):
        omdb_movie_client = OmdbMovieClient()

        movies = omdb_movie_client.get_movies_for(["3 idiots"])

        self.assertEqual("9/10", movies[0].rating_value_at(0))
