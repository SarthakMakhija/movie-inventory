from functools import wraps

from flask import request

from core.json_.json_deserializer import Json


def deserialize(target: type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            payload = request.json
            return func(*args, Json.of(payload).deserialize_to(target))
        return wrapper

    return decorator
