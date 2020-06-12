import unittest

from flask_restful import Resource

from flaskr import application_ref
from tests.fixtures.test_client import TestClient


class MovieSnapshotTest(unittest.TestCase):

    def test_should_return_Ok_given_a_request_to_get_all_movie_snapshots(self):
        response = TestClient.create().get("/movie-snapshots")
        self.assertEqual(200, response.status_code)


class MovieSnapshots(Resource):

    def get(self):
        return {}


application_ref.api.add_resource(MovieSnapshots, "/movie-snapshots")
