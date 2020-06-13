import unittest
from datetime import date

from flaskr.view.movie_snapshots_view import MovieSnapshotsView
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder


class MovieSnapshotsViewTest(unittest.TestCase):

    def test_should_create_movie_snapshot_view_with_title(self):
        movie_snapshot = MovieSnapshotsBuilder.snapshot_title("3 idiots").finish()
        movie_snapshot_view = MovieSnapshotsView.make_from(movie_snapshot)
        self.assertEqual("3 idiots", movie_snapshot_view.title)

    def test_should_create_movie_snapshot_view_with_director(self):
        movie_snapshot = MovieSnapshotsBuilder.any_snapshot().directed_by("Rajkumar").finish()
        movie_snapshot_view = MovieSnapshotsView.make_from(movie_snapshot)
        self.assertEqual("Rajkumar", movie_snapshot_view.director)

    def test_should_create_movie_snapshot_view_with_release_date(self):
        movie_snapshot = MovieSnapshotsBuilder.any_snapshot().released_on(date(2015, 12, 25)).finish()
        movie_snapshot_view = MovieSnapshotsView.make_from(movie_snapshot)
        self.assertEqual(date(2015, 12, 25).isoformat(), movie_snapshot_view.release_date)

    def test_should_create_movie_snapshot_view_with_release_year(self):
        movie_snapshot = MovieSnapshotsBuilder.any_snapshot().released_on(date(2015, 12, 25)).finish()
        movie_snapshot_view = MovieSnapshotsView.make_from(movie_snapshot)
        self.assertEqual(2015, movie_snapshot_view.release_year)

    def test_should_create_movie_snapshot_view_with_a_rating_from_internet(self):
        movie_snapshot = MovieSnapshotsBuilder.any_snapshot().add_rating_with("", "internet").finish()
        movie_snapshot_view = MovieSnapshotsView.make_from(movie_snapshot)
        self.assertEqual("internet", movie_snapshot_view.ratings[0].source)

    def test_should_create_movie_snapshot_view_with_a_rating_of_7_on_10(self):
        movie_snapshot = MovieSnapshotsBuilder.any_snapshot().add_rating_with("7/10", "").finish()
        movie_snapshot_view = MovieSnapshotsView.make_from(movie_snapshot)
        self.assertEqual("7/10", movie_snapshot_view.ratings[0].value)
