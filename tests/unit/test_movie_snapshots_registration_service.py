import unittest
from unittest.mock import patch

from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.service.movie_snapshots_registration_service import MovieSnapshotsRegistrationService


class MovieSnapshotsRegistrationServiceTest(unittest.TestCase):

    @patch("flaskr.service.movie_snapshots_registration_service.requests.get")
    def test_should_fetch_movies_to_be_registered_as_snapshots_given_registration_request(self, get_requests_mock):
        movie_snapshots_registration_request = MovieSnapshotsRegistrationRequest(titles=["3 idiots"])
        movie_snapshots_registration_service = MovieSnapshotsRegistrationService()

        movie_snapshots_registration_service.register_snapshots_for(movie_snapshots_registration_request)
        get_requests_mock.assert_called_once_with("http://www.omdbapi.com/?t=3 idiots")
