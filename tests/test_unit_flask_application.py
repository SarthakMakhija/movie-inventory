import unittest

from flaskr.configuration import Configuration
from flaskr.flask_application import Application
from tests.application_test import application_test


@application_test()
class ApplicationTest(unittest.TestCase):

    def test_should_return_an_instance_of_app_with_configuration(self):
        class TestConfiguration(Configuration):
            ENV = "TEST"
            SQLALCHEMY_DATABASE_URI = ""

        app = Application.create_app(TestConfiguration)
        env = app.config.get("ENV")
        self.assertEqual("TEST", env)
