from typing import TypeVar

from flaskr.model.response import Success, Response

T = TypeVar("T")


class ResponseBuilder:

    @staticmethod
    def successful_response_with(t: T) -> Response:
        response = Response()
        response.add(Success.of(t))
        return response

    @staticmethod
    def any_response() -> Response:
        return Response()
