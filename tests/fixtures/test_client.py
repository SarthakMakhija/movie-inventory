from flaskr.flask_application import Application
from tests.configuration.configuration_test import TestConfiguration


class TestClient:
    @staticmethod
    def create():
        return Application(TestConfiguration).flask_application.test_client()
