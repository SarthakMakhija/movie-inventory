from flask import current_app as app


class TestClient:
    @staticmethod
    def create():
        return app.test_client()
