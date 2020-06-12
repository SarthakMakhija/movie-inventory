import unittest
from logging import Logger

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flaskr.configuration import Configuration
from flaskr.flask_application import Application


class ApplicationTest(unittest.TestCase):

    def test_should_return_an_instance_of_app_with_api_reference(self):
        application = Application.create_app(Configuration)
        api = application.api
        self.assertTrue(type(api) == Api)

    def test_should_return_an_instance_of_app_with_db_reference(self):
        application = Application.create_app(Configuration)
        app = application.db
        self.assertTrue(type(app) == SQLAlchemy)

    def test_should_return_an_instance_of_app_with_logger_reference(self):
        application = Application.create_app(Configuration)
        app = application.logger
        self.assertTrue(type(app) == Logger)

    def test_should_return_an_instance_of_app_with_configuration(self):

        class TestConfiguration(Configuration):
            ENV = "TEST"

        application = Application.create_app(TestConfiguration)
        env = application.configuration_value_for("ENV")
        self.assertEqual("TEST", env)
