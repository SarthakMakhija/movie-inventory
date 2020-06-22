import unittest

from flask_restful import Resource

from flaskr.security.authentication import authenticate
from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration
from tests.integration import application
from tests.test_client import add_test_client


@application_test()
@add_test_client()
class AuthenticationTest(unittest.TestCase):

    def test_should_return_Unauthorized_given_request_does_not_contain_authorization_header(self):
        response = self.test_client.get("/fake-protected")
        status_code = response.status_code
        self.assertEqual(401, status_code)

    def test_should_return_Ok_given_request_contains_authorization_header(self):
        response = self.test_client.get("/fake-protected", headers=[("x-api-key", TestConfiguration.X_API_KEY)])
        status_code = response.status_code
        self.assertEqual(200, status_code)


class FakeProtectedResource(Resource):
    method_decorators = [authenticate]

    def get(self):
        return {}


application.api.add_resource(FakeProtectedResource, "/fake-protected")
