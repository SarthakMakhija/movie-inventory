from http import HTTPStatus

from flask import request
from flask_restful import abort

from core.config.application_config import ApplicationConfig


def authenticate(func):
    def wrapper(*args, **kargs):
        authorization_header = request.headers.get("x-api-key", "")
        application_config = ApplicationConfig.instance()
        x_api_key = application_config.get_or_fail("X_API_KEY")

        if authorization_header == "" or authorization_header != x_api_key:
            abort(HTTPStatus.UNAUTHORIZED)
        return func(*args, **kargs)

    return wrapper
