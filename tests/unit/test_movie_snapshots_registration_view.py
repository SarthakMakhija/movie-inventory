import unittest

from flaskr.model.movie_registration_snapshots_response import MovieSnapshotsRegistrationResponse
from flaskr.model.registered_snapshot import RegisteredSnapshot
from flaskr.view.movie_snapshots_registration_view import MovieSnapshotsRegistrationView


class MovieSnapshotsRegistrationViewTest(unittest.TestCase):

    def test_should_return_registered_snapshots_with_id(self):
        movie_snapshot_registration_response = \
            MovieSnapshotsRegistrationResponse(registered_snapshots=[RegisteredSnapshot(1200, "")])

        movie_snapshot_registration_view = MovieSnapshotsRegistrationView.make_from(movie_snapshot_registration_response)
        self.assertEqual(1200, movie_snapshot_registration_view.registered_snapshots[0]["id"])

    def test_should_return_registered_snapshots_with_title(self):
        movie_snapshot_registration_response = \
            MovieSnapshotsRegistrationResponse(registered_snapshots=[RegisteredSnapshot(1200, "3 idiots")])

        movie_snapshot_registration_view = MovieSnapshotsRegistrationView.make_from(movie_snapshot_registration_response)
        self.assertEqual("3 idiots", movie_snapshot_registration_view.registered_snapshots[0]["title"])

    def test_should_return_registration_failure_titles(self):
        movie_snapshot_registration_response = \
            MovieSnapshotsRegistrationResponse(registered_snapshots=[], registration_failure_titles=["3 idiots"])

        movie_snapshot_registration_view = MovieSnapshotsRegistrationView.make_from(movie_snapshot_registration_response)
        self.assertEqual("3 idiots", movie_snapshot_registration_view.registration_failure_titles[0])
