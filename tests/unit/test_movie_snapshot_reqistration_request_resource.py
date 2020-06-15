import unittest

from tests.fixtures.test_client import TestClient


class MovieSnapshotsRegistrationRequestResource(unittest.TestCase):
    __test_client = TestClient.create()

    def test_should_return_Created_given_a_request_to_register_movie_snapshots(self):

        response = self.__test_client.post("/movie-snapshots/registration-request",
                                           data='{"titles": ["3 idiots"]}',
                                           content_type="application/json")

        self.assertEqual(201, response.status_code)
