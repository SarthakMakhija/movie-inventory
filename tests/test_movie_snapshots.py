import unittest
from unittest.mock import patch

from tests.fixtures.test_client import TestClient


class MovieSnapshotTests(unittest.TestCase):

    __test_client = TestClient.create()

    @patch("flaskr.resource.movie_snapshots.MovieSnapshotsService")
    def test_should_return_Ok_given_a_request_to_get_all_movie_snapshots(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get.return_value = []
        response = self.__test_client.get("/movie-snapshots")
        self.assertEqual(200, response.status_code)

    @patch("flaskr.resource.movie_snapshots.MovieSnapshotsService")
    def test_should_return_no_snapshots_given_no_snapshots_exist(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get.return_value = []
        response = self.__test_client.get("/movie-snapshots")
        self.assertEqual([], response.json)

    @patch("flaskr.resource.movie_snapshots.MovieSnapshotsService")
    def test_should_assert_total_snapshots_to_equal_1(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get.return_value = [{}]
        response = self.__test_client.get("/movie-snapshots")
        movie_snapshots = response.json
        self.assertEqual(len(movie_snapshots), 1)
