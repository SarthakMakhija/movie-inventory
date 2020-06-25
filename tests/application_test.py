from flaskr.flask_application import Application
from tests.configuration.configuration_test import TestConfiguration


def application_test():
    def decorator(test_item):
        app = Application.create_app(TestConfiguration)
        app.app_context().push()
        return test_item

    return decorator
