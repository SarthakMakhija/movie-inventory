import unittest
from datetime import date

from flaskr.entity.movie_snapshot import MovieSnapshot
from flaskr.omdb_movie_client import Movie


class MovieTest(unittest.TestCase):
    movie = Movie({
        "Title": "3 idiots",
        "Director": "Rajkumar Hirani",
        "Released": "25 Dec 2009",
        "Ratings": [{"Source": "internet", "Value": "9/10"}]}
    )

    def test_should_return_a_movie_snapshot_with_title(self):
        movie_snapshot: MovieSnapshot = self.movie.to_movie_snapshot()
        self.assertEqual("3 idiots", movie_snapshot.title)

    def test_should_return_a_movie_snapshot_with_director(self):
        movie_snapshot: MovieSnapshot = self.movie.to_movie_snapshot()
        self.assertEqual("Rajkumar Hirani", movie_snapshot.director)

    def test_should_return_a_movie_snapshot_with_release_date(self):
        movie_snapshot: MovieSnapshot = self.movie.to_movie_snapshot()
        self.assertEqual(date(2009, 12, 25), movie_snapshot.release_date)

    def test_should_return_a_movie_snapshot_with_single_rating(self):
        movie_snapshot: MovieSnapshot = self.movie.to_movie_snapshot()
        self.assertEqual(1, len(movie_snapshot.ratings))

    def test_should_return_a_movie_snapshot_with_rating_source(self):
        movie_snapshot: MovieSnapshot = self.movie.to_movie_snapshot()
        self.assertEqual("internet", movie_snapshot.ratings[0].source)

    def test_should_return_a_movie_snapshot_with_rating_value(self):
        movie_snapshot: MovieSnapshot = self.movie.to_movie_snapshot()
        self.assertEqual("9/10", movie_snapshot.ratings[0].value)
