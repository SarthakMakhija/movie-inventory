import unittest
from logging import Logger

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flaskr.application import Application


class ApplicationTest(unittest.TestCase):

    def test_should_return_an_instance_of_api(self):
        application = Application()
        api = application.api
        self.assertTrue(type(api) == Api)

    def test_should_return_an_instance_of_app(self):
        application = Application()
        app = application.app
        self.assertTrue(type(app) == Flask)

    def test_should_return_an_instance_of_logger(self):
        application = Application()
        logger = application.logger
        self.assertTrue(type(logger) == Logger)

    def test_should_return_an_instance_of_SQLAlchemy(self):
        application = Application()
        db = application.db
        self.assertTrue(type(db) == SQLAlchemy)
