import unittest
from datetime import date
from typing import List

from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository
from tests.application_test import application_test
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder
from tests.fixtures.movie_snapshots_fixture import MovieSnapshotsFixture


@application_test()
class MovieSnapshotsResourceRepositoryIntegrationTest(unittest.TestCase):

    def test_should_save_all_movie_snapshots(self):
        movie_snapshot = MovieSnapshotsBuilder.snapshot_title("3 idiots") \
            .directed_by("Rajkumar") \
            .released_on(date(2019, 12, 25)) \
            .add_rating_with("7/10", "internet") \
            .finish()

        snapshot_ids: List[int] = MovieSnapshotsRepository().save_all([movie_snapshot])
        snapshot_id = snapshot_ids[0]

        movie_snapshot = MovieSnapshotsFixture.get_by_id(snapshot_id)

        self.assertIsNotNone(snapshot_id)
        self.assertEqual("3 idiots", movie_snapshot.title)
        self.assertEqual("Rajkumar", movie_snapshot.director)
        self.assertEqual(date(2019, 12, 25), movie_snapshot.release_date)
        self.assertEqual("internet", movie_snapshot.ratings[0].source)
        self.assertEqual("7/10", movie_snapshot.ratings[0].value)

    def tearDown(self) -> None:
        MovieSnapshotsFixture.delete_all()
