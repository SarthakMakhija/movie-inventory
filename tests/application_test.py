from flaskr.flask_application import Application
from tests.configuration.configuration_test import TestConfiguration


def application_test():
    def decorator(test_item):
        Application.init_app(TestConfiguration)
        return test_item

    return decorator
