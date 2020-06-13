import unittest

from flask_restful import Resource

from flaskr.security.authentication import authenticate
from tests.fixtures.test_client import TestClient
from tests.integration import application


class AuthenticationTest(unittest.TestCase):
    __test_client = TestClient.create()

    def test_should_return_Unauthorized_given_request_does_not_contain_authorization_header(self):
        response = self.__test_client.get("/fake-protected")
        status_code = response.status_code
        self.assertEqual(401, status_code)

    def test_should_return_Ok_given_request_contains_authorization_header(self):
        response = self.__test_client.get("/fake-protected", headers=[("Authorization", "fake")])
        status_code = response.status_code
        self.assertEqual(200, status_code)


class FakeProtectedResource(Resource):
    method_decorators = [authenticate]

    def get(self):
        return {}


application.api.add_resource(FakeProtectedResource, "/fake-protected")
