import unittest
from logging import Logger

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flaskr import Application


class ApplicationTest(unittest.TestCase):

    def test_should_return_an_instance_of_api(self):
        application = Application(app=Flask(__name__))
        api = application.api
        self.assertTrue(type(api) == Api)

    def test_should_return_an_instance_of_app(self):
        application = Application(app=Flask(__name__))
        app = application.app
        self.assertTrue(type(app) == Flask)

    def test_should_return_an_instance_of_logger(self):
        application = Application(app=Flask(__name__))
        logger = application.logger
        self.assertTrue(type(logger) == Logger)

    def test_should_return_an_instance_of_SQLAlchemy(self):
        application = Application(app=Flask(__name__))
        db = application.db
        self.assertTrue(type(db) == SQLAlchemy)
