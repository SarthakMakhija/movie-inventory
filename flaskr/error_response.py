class HTTPErrorResponse:

    def __init__(self, status, message):
        self.__status = status
        self.__message = message

    def json(self) -> dict:
        return {
            "status": self.__status,
            "message": self.__message
        }
