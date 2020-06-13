import json
import textwrap
import unittest
from datetime import date

from flask_restful import marshal

from flaskr.entity.movie_snapshot import MovieSnapshot, MovieSnapshotRating
from flaskr.view.movie_snapshots_view import MovieSnapshotsView, MovieSnapshotRatingsView
from tests.fixtures.movie_snapshot_fixture import MovieSnapshotFixture
from tests.fixtures.test_client import TestClient


class MovieSnapshotResourceTest(unittest.TestCase):
    __test_client = TestClient.create()

    def test_should_assert_all_snapshots(self):
        MovieSnapshotFixture.create_a_movie_snapshot(MovieSnapshot("3 idiots", "Rajkumar Hirani",
                                                                   date(2009, 12, 25),
                                                                   [MovieSnapshotRating(value="7/10",
                                                                                        source="internet"),
                                                                    MovieSnapshotRating(value="9/10", source="imdb")]))

        expected_json = '[{"title": "3 idiots", "director": "Rajkumar Hirani", "release_year": 2009, "release_date": ' \
                        '"2009-12-25", "ratings": [{"value": "internet", "source": "7/10"}, {"value": "imdb", ' \
                        '"source": "9/10"}]}]'

        expected_movie_snapshot_views = json.loads(expected_json)

        response = self.__test_client.get("/movie-snapshots")

        actual_movie_snapshot_views = response.json
        self.assertEqual(expected_movie_snapshot_views, actual_movie_snapshot_views)

    def tearDown(self) -> None:
        MovieSnapshotFixture.delete_all()
