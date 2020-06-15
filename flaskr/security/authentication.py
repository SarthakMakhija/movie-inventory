from flask import request
from flask_restful import abort


def authenticate(func):
    def wrapper(*args, **kargs):
        from flaskr.flask_application import Application
        authorization_header = request.headers.get("x-api-key", "")
        x_api_key = Application.instance().configuration_value_for("X_API_KEY")

        if authorization_header == "" or authorization_header != x_api_key:
            abort(401)
        return func(*args, **kargs)

    return wrapper
