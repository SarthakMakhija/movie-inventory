from http import HTTPStatus

from flask import request
from flask_restful import abort

from flask import current_app as app


def authenticate(func):
    def wrapper(*args, **kargs):
        authorization_header = request.headers.get("x-api-key", "")
        x_api_key = app.config.get("X_API_KEY")

        if authorization_header == "" or authorization_header != x_api_key:
            abort(HTTPStatus.UNAUTHORIZED)
        return func(*args, **kargs)

    return wrapper
