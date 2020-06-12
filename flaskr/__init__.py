from flask import Flask

from flaskr.application import Application

__app = Flask(__name__)


def create_app():
    return __app


application_ref = Application(__app)
