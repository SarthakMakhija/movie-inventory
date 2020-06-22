from flaskr.flask_application import Application


class TestClient:
    @staticmethod
    def create():
        return Application.instance().flask_application.test_client()
