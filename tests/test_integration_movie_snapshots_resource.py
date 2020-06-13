import unittest

from flask_restful import marshal

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.view.movie_snapshots_view import MovieSnapshotsView
from tests.fixtures.movie_snapshot_fixture import MovieSnapshotFixture
from tests.fixtures.test_client import TestClient


class MovieSnapshotResourceTest(unittest.TestCase):
    __test_client = TestClient.create()

    def test_should_assert_all_snapshots(self):
        MovieSnapshotFixture.create_a_movie_snapshot(MovieSnapshot("3 idiots", "Rajkumar Hirani"))

        expected_movie_snapshots_views = marshal([MovieSnapshotsView("3 idiots", "Rajkumar Hirani")],
                                                 fields=MovieSnapshotsView.DISPLAYABLE_FIELDS)

        response = self.__test_client.get("/movie-snapshots")

        actual_movie_snapshot_views = response.json
        self.assertEqual(expected_movie_snapshots_views, actual_movie_snapshot_views)

    def tearDown(self) -> None:
        MovieSnapshotFixture.delete_all()

