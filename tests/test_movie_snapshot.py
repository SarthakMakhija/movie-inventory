import unittest

from tests.fixtures.test_client import TestClient


class MovieSnapshotTest(unittest.TestCase):

    def test_should_return_Ok_given_a_request_to_get_all_movie_snapshots(self):
        response = TestClient.create().get("/movie-snapshots")
        self.assertEqual(200, response.status_code)

    def test_should_return_no_snapshots_given_no_snapshots_exist(self):
        response = TestClient.create().get("/movie-snapshots")
        self.assertEqual([], response.json)
