import unittest

from flaskr.service.movie_snapshots_service import MovieSnapshotsService


class MovieSnapshotsServiceTest(unittest.TestCase):

    def test_should_return_zero_movie_snapshots(self):
        movie_snapshots = MovieSnapshotsService().get_all()
        self.assertEqual(0, len(movie_snapshots))

