from ipe_core.application.core_application import CoreApplication


class TestClient:
    @staticmethod
    def create():
        return CoreApplication.instance().flask_application.test_client()
