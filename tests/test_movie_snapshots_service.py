import unittest
from unittest.mock import patch

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.service.movie_snapshots_service import MovieSnapshotsService


class MovieSnapshotsServiceTest(unittest.TestCase):

    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository")
    def test_should_return_zero_movie_snapshots(self, movie_snapshots_repository):
        movie_snapshots_repository.return_value.get_all.return_value = []
        movie_snapshots = MovieSnapshotsService().get_all()
        self.assertEqual(0, len(movie_snapshots))

    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository")
    def test_should_return_one_movie_snapshot(self, movie_snapshots_repository):
        movie_snapshots_repository.return_value.get_all.return_value = [{}]
        movie_snapshots = MovieSnapshotsService().get_all()
        self.assertEqual(1, len(movie_snapshots))

    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository")
    def test_should_return_one_movie_snapshot_with_movie_title(self, movie_snapshots_repository):
        movie_snapshots_repository.return_value.get_all.return_value = [MovieSnapshot(title="3 idiots", director="")]
        movie_snapshot: MovieSnapshot = MovieSnapshotsService().get_all()[0]
        self.assertEqual("3 idiots", movie_snapshot.title)

    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository")
    def test_should_return_one_movie_snapshot_with_movie_director(self, movie_snapshots_repository):
        movie_snapshots_repository.return_value.get_all.return_value = [MovieSnapshot(title="", director="Rajkumar")]
        movie_snapshot: MovieSnapshot = MovieSnapshotsService().get_all()[0]
        self.assertEqual("Rajkumar", movie_snapshot.director)
