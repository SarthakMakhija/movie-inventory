from __future__ import annotations

from typing import TypeVar

from flaskr.model.response import Success, Response, Failure

T = TypeVar("T")
E = TypeVar("E")


class ResponseBuilder:

    def __init__(self):
        self.__response = Response()

    def successful_response_with(self, t: T) -> ResponseBuilder:
        self.__response.add(Success.of(t))
        return self

    def failure_response_with(self, t: T) -> ResponseBuilder:
        self.__response.add(Failure.of(t))
        return self

    def empty_response(self) -> ResponseBuilder:
        return self

    def finish(self) -> Response[T, E]:
        return self.__response
