import unittest

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flaskr.configuration import Configuration
from flaskr.flask_application import Application
from tests.application_test import application_test
from tests.configuration.configuration_test import TestConfiguration


@application_test()
class ApplicationTest(unittest.TestCase):

    def test_should_return_an_instance_of_app_with_api_reference(self):
        application = Application.init_app(TestConfiguration)
        api = application.api
        self.assertTrue(type(api) == Api)

    def test_should_return_an_instance_of_app_with_db_reference(self):
        application = Application.init_app(TestConfiguration)
        app = application.db
        self.assertTrue(type(app) == SQLAlchemy)

    def test_should_return_an_instance_of_app_with_configuration(self):
        class TestConfiguration(Configuration):
            ENV = "TEST"
            SQLALCHEMY_DATABASE_URI = ""

        application = Application.init_app(TestConfiguration)
        env = application.configuration_value_for("ENV")
        self.assertEqual("TEST", env)
