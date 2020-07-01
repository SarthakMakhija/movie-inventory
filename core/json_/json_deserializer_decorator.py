from functools import wraps

from flask import request

from core.json_.json_deserializer import Json


def deserialize(target: type, strict_mode: bool = True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            payload = request.json

            if payload is None and not strict_mode:
                return func(*args, None)

            return func(*args, Json.of(payload).deserialize_to(target))

        return wrapper

    return decorator
