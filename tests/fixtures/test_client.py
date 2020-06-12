from flaskr.flask_application import Application
from tests.configuration.TestConfiguration import TestConfiguration


class TestClient:
    @staticmethod
    def create():
        return Application(TestConfiguration).flask_application.test_client()
