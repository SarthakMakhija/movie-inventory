import unittest
from unittest.mock import patch, call

from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.service.movie_snapshots_registration_service import MovieSnapshotsRegistrationService


class MovieSnapshotsRegistrationServiceTest(unittest.TestCase):

    @patch("flaskr.service.movie_snapshots_registration_service.requests.get")
    def test_should_fetch_single_movie_to_be_registered_as_snapshots_given_registration_request(self,
                                                                                                get_requests_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        get_requests_mock.assert_called_once_with("http://www.omdbapi.com/?t=3 idiots")

    @patch("flaskr.service.movie_snapshots_registration_service.requests.get")
    def test_should_fetch_movies_to_be_registered_as_snapshots_given_registration_request(self, get_requests_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots", "Jumanji"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        get_requests_mock.assert_has_calls([call("http://www.omdbapi.com/?t=3 idiots"),
                                            call().json(),
                                            call("http://www.omdbapi.com/?t=Jumanji"),
                                            call().json()],
                                           any_order=False)

    @patch("flaskr.service.movie_snapshots_registration_service.requests.get")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_register_movie_snapshots_given_registration_request(self, save_all_movie_snapshots_repository_mock,
                                                                        get_requests_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        ratings = [{"Source": "Internet Movie Database",
                    "Value": "8.4/10"
                    }]
        get_requests_mock.return_value.json.return_value = {"Title": "3 Idiots",
                                                            "Director": "Rajkumar Hirani",
                                                            "Released": "25 Dec 2009",
                                                            "Ratings": ratings}

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        save_all_movie_snapshots_repository_mock.assert_called_once()
