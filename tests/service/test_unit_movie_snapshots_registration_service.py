import unittest
from unittest.mock import patch

from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.omdb_movie_client import Movie
from flaskr.service.movie_snapshots_registration_service import MovieSnapshotsRegistrationService
from tests.application_test import application_test
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder
from tests.fixtures.response_builder import ResponseBuilder


@application_test()
class MovieSnapshotsRegistrationServiceTest(unittest.TestCase):

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_response_for")
    def test_should_fetch_movies_given_registration_request(self,
                                                            get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = ResponseBuilder().empty_response().finish()

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        get_movies_omdb_client_mock.called_once_with(["3 idiots"])

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_response_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_register_movie_snapshots_given_registration_request(self,
                                                                        save_all_movie_snapshots_repository_mock,
                                                                        get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = ResponseBuilder().successful_response_with(Movie({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]}
        )).finish()

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        save_all_movie_snapshots_repository_mock.assert_called_once()

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_response_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_not_register_movie_snapshots_given_no_movie_exists_for_the_given_title(self,
                                                                                           save_all_movie_snapshots_repository_mock,
                                                                                           get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = ResponseBuilder().failure_response_with("3 idiots").finish()

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        save_all_movie_snapshots_repository_mock.assert_not_called()

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_response_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_return_movie_registration_response_with_failures_given_there_was_no_snapshot_to_be_registered(self,
                                                                                                                  save_all_movie_snapshots_repository_mock,
                                                                                                                  get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = ResponseBuilder().failure_response_with("3 idiots").finish()

        movie_snapshot_registration_response = movie_snapshots_registration_service.register_snapshots_for(
            movie_snapshots_registration_request)

        self.assertEqual(["3 idiots"], movie_snapshot_registration_response.registration_failure_titles)

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_response_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_return_movie_registration_response_with_snapshot_ids(self,
                                                                         save_all_movie_snapshots_repository_mock,
                                                                         get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = ResponseBuilder().successful_response_with(Movie({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]}
        )).finish()

        save_all_movie_snapshots_repository_mock.return_value = [MovieSnapshotsBuilder
                                                                     .snapshot_title("3 idiots")
                                                                     .snapshot_id("id_001")
                                                                     .finish()]

        movie_snapshot_registration_response = movie_snapshots_registration_service.register_snapshots_for(
            movie_snapshots_registration_request)

        self.assertEqual(["id_001"], movie_snapshot_registration_response.registered_snapshot_ids)

    @patch("flaskr.service.movie_snapshots_registration_service.OmdbMovieClient.get_movies_response_for")
    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository.save_all")
    def test_should_return_movie_registration_response_with_snapshot_ids(self,
                                                                         save_all_movie_snapshots_repository_mock,
                                                                         get_movies_omdb_client_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        get_movies_omdb_client_mock.return_value = ResponseBuilder().successful_response_with(Movie({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]}
        )).finish()

        save_all_movie_snapshots_repository_mock.return_value = [MovieSnapshotsBuilder
                                                                     .snapshot_title("3 idiots")
                                                                     .finish()]

        movie_snapshot_registration_response = movie_snapshots_registration_service.register_snapshots_for(
            movie_snapshots_registration_request)

        self.assertEqual(["3 idiots"], movie_snapshot_registration_response.registered_snapshot_titles)
