import unittest

from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder
from tests.fixtures.movie_snapshots_fixture import MovieSnapshotsFixture
from tests.fixtures.test_client import TestClient


class MovieSnapshotsResourceRepositoryIntegrationTest(unittest.TestCase):
    __client = TestClient.create()

    def test_should_save_all_movie_snapshots(self):
        movie_snapshot = MovieSnapshotsBuilder.any_snapshot().finish()
        snapshot_ids = MovieSnapshotsRepository().save_all([movie_snapshot])
        self.assertIsNotNone(snapshot_ids[0])

    def tearDown(self) -> None:
        MovieSnapshotsFixture.delete_all()