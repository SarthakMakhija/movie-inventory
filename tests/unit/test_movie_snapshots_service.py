import unittest
from datetime import date
from unittest.mock import patch

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.service.movie_snapshots_service import MovieSnapshotsService
from tests.application_test import application_test
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder


@application_test()
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
        movie_snapshots_repository.return_value.get_all.return_value = [
            MovieSnapshotsBuilder.snapshot_title("3 idiots").finish()]

        movie_snapshot: MovieSnapshot = MovieSnapshotsService().get_all()[0]
        self.assertEqual("3 idiots", movie_snapshot.title)

    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository")
    def test_should_return_one_movie_snapshot_with_movie_director(self, movie_snapshots_repository):
        movie_snapshots_repository.return_value.get_all.return_value = [
            MovieSnapshotsBuilder.any_snapshot().directed_by("Rajkumar").finish()]

        movie_snapshot: MovieSnapshot = MovieSnapshotsService().get_all()[0]
        self.assertEqual("Rajkumar", movie_snapshot.director)

    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository")
    def test_should_return_one_movie_snapshot_with_release_date(self, movie_snapshots_repository):
        movie_snapshots_repository.return_value.get_all.return_value = [
            MovieSnapshotsBuilder.any_snapshot().released_on(date(2009, 12, 25)).finish()]

        movie_snapshot: MovieSnapshot = MovieSnapshotsService().get_all()[0]
        self.assertEqual(date(2009, 12, 25), movie_snapshot.release_date)

    @patch("flaskr.service.movie_snapshots_service.MovieSnapshotsRepository")
    def test_should_return_one_movie_snapshot_with_release_year(self, movie_snapshots_repository):
        movie_snapshots_repository.return_value.get_all.return_value = [
            MovieSnapshotsBuilder.any_snapshot().released_on(date(2009, 12, 25)).finish()]

        movie_snapshot: MovieSnapshot = MovieSnapshotsService().get_all()[0]
        self.assertEqual(2009, movie_snapshot.release_year)
