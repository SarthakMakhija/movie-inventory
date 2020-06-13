from tests.integration import app


class TestClient:
    @staticmethod
    def create():
        return app.test_client()
