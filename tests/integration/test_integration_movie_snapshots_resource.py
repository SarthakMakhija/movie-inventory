import json
import unittest
from datetime import date

from tests.application_test import application_test
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder
from tests.fixtures.movie_snapshots_fixture import MovieSnapshotsFixture
from tests.test_client import add_test_client


@application_test()
@add_test_client()
class MovieSnapshotsResourceIntegrationTest(unittest.TestCase):

    def test_should_assert_all_snapshots(self):
        movie_snapshot = MovieSnapshotsBuilder.snapshot_title("3 idiots") \
            .directed_by("Rajkumar Hirani") \
            .released_on(date(2009, 12, 25)) \
            .add_rating_with(value="7/10", source="internet") \
            .add_rating_with(value="9/10", source="imdb") \
            .finish()

        MovieSnapshotsFixture.create_a_movie_snapshot(movie_snapshot)

        expected_json = '[{"title": "3 idiots", "director": "Rajkumar Hirani", "release_year": 2009, "release_date": ' \
                        '"2009-12-25", "ratings": [{"value": "7/10", "source": "internet"}, {"value": "9/10", ' \
                        '"source": "imdb"}]}]'

        expected_movie_snapshot_views = json.loads(expected_json)

        response = self.test_client.get("/movie-snapshots")

        actual_movie_snapshot_views = response.json
        self.assertEqual(expected_movie_snapshot_views, actual_movie_snapshot_views)

    def tearDown(self) -> None:
        MovieSnapshotsFixture.delete_all()
