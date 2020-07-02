from typing import Type

from flaskr.error_response import HTTPErrorResponse


class ErrorRegistry:
    errors: dict = {}

    @classmethod
    def register_error(cls, exception_type: Type[Exception], error_response: HTTPErrorResponse):
        cls.errors[exception_type.__name__] = error_response.json()
