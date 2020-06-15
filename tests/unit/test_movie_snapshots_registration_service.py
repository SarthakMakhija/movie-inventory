import unittest
from unittest.mock import patch

from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.omdb_movie_client import Movie
from flaskr.service.movie_snapshots_registration_service import MovieSnapshotsRegistrationService


class MovieSnapshotsRegistrationServiceTest(unittest.TestCase):

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_for")
    def test_should_fetch_movies_given_registration_request(self,
                                                            get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = []

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        get_movies_omdb_client_mock.called_once_with(["3 idiots"])

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_register_movie_snapshots_given_registration_request(self,
                                                                        save_all_movie_snapshots_repository_mock,
                                                                        get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = [Movie({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]}
        )]

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        save_all_movie_snapshots_repository_mock.assert_called_once()

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_not_register_movie_snapshots_given_no_movie_exists_for_the_given_title(self,
                                                                                           save_all_movie_snapshots_repository_mock,
                                                                                           get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = []

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        save_all_movie_snapshots_repository_mock.assert_not_called()

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_return_empty_list_of_movie_snapshot_ids_given_no_registration_was_done(self,
                                                                                           save_all_movie_snapshots_repository_mock,
                                                                                           get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = []

        movie_snapshot_registration_response = movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        self.assertEqual([], movie_snapshot_registration_response)

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_return_a_list_of_registered_movie_snapshot_ids(self,
                                                                   save_all_movie_snapshots_repository_mock,
                                                                   get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = [Movie({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]}
        )]
        save_all_movie_snapshots_repository_mock.return_value = ["id_001"]

        movie_snapshot_registration_response = movie_snapshots_registration_service.register_snapshots_for(
            movie_snapshots_registration_request)

        self.assertEqual(["id_001"], movie_snapshot_registration_response)
