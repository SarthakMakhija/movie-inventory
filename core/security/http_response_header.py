from dataclasses import dataclass
from typing import List

from flask import Response


@dataclass(frozen=True)
class HttpResponseHeader:
    name: str
    value: str


class HttpResponseHeaders:
    def __init__(self, http_response_headers: List[HttpResponseHeader]):
        self.__http_response_headers = http_response_headers

    def copy_in(self, response: Response) -> Response:
        for http_response_header in self.__http_response_headers:
            response.headers[http_response_header.name] = http_response_header.value

        return response
