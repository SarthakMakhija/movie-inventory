from main import app


class TestClient:
    @staticmethod
    def create():
        return app.app.test_client()
