import unittest

from flaskr.model.registered_snapshot import RegisteredSnapshot
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder


class RegisteredSnapshotTest(unittest.TestCase):

    def test_should_create_a_registered_snapshot_with_snapshot_id(self):
        registered_snapshot = RegisteredSnapshot.make_from(
            MovieSnapshotsBuilder.any_snapshot().snapshot_id(1000).finish()
        )
        self.assertEqual(1000, registered_snapshot.snapshot_id)

    def test_should_create_a_registered_snapshot_with_snapshot_title(self):
        registered_snapshot = RegisteredSnapshot.make_from(
            MovieSnapshotsBuilder.snapshot_title("3 idiots").finish()
        )
        self.assertEqual("3 idiots", registered_snapshot.snapshot_title)
