import unittest
from datetime import date
from unittest.mock import patch

from flask_restful import marshal

from flaskr.view.movie_snapshots_view import MovieSnapshotsView
from tests.fixtures.movie_snapshot_builder import MovieSnapshotBuilder
from tests.fixtures.test_client import TestClient


class MovieSnapshotResourceTest(unittest.TestCase):
    __test_client = TestClient.create()

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_return_Ok_given_a_request_to_get_all_movie_snapshots(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get_all.return_value = []
        response = self.__test_client.get("/movie-snapshots")
        self.assertEqual(200, response.status_code)

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_return_no_snapshots_given_no_snapshots_exist(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get_all.return_value = []
        response = self.__test_client.get("/movie-snapshots")
        self.assertEqual([], response.json)

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_assert_total_snapshots_to_equal_1(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get_all.return_value = [MovieSnapshotBuilder.any_snapshot().finish()]
        response = self.__test_client.get("/movie-snapshots")
        movie_snapshots = response.json
        self.assertEqual(1, len(movie_snapshots))

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_assert_all_snapshots(self, movie_snapshots_service):
        movie_snapshot = MovieSnapshotBuilder.snapshot_title("3 idiots") \
            .directed_by("Rajkumar Hirani") \
            .released_on(date(2009, 12, 25)) \
            .finish()

        expected_movie_snapshots_views = marshal(
            [MovieSnapshotsView("3 idiots", "Rajkumar Hirani", date(2009, 12, 25))],
            fields=MovieSnapshotsView.DISPLAYABLE_FIELDS)

        movie_snapshots = [movie_snapshot]
        movie_snapshots_service.return_value.get_all.return_value = movie_snapshots

        response = self.__test_client.get("/movie-snapshots")
        actual_movie_snapshot_views = response.json
        self.assertEqual(expected_movie_snapshots_views, actual_movie_snapshot_views)
