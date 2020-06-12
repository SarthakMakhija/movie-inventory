from flaskr import application_ref


class TestClient:
    @staticmethod
    def create():
        return application_ref.app.test_client()
