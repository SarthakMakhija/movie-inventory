from flask import request
from flask_restful import abort


def authenticate(func):
    def wrapper(*args, **kargs):
        authorization_header = request.headers.get("Authorization", "")
        ##TODO:: Add logic to check for a fixed value of header
        if authorization_header == "":
            abort(401)
        return func(*args, **kargs)

    return wrapper
