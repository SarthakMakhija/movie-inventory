from http import HTTPStatus


class HTTPErrorResponse:

    def __init__(self, status_code: HTTPStatus, message: str):
        self.__status_code = status_code
        self.__message = message

    def json(self) -> dict:
        return {
            "status": self.__status_code,
            "message": self.__message
        }
