from jsons import DeserializationError


class JsonDeserializationException(Exception):

    def __init__(self, message: str, source: object, target: type):
        self.__message = message
        self.__source = source
        self.__target = target

    @staticmethod
    def make_from(deserialization_error: DeserializationError):
        return JsonDeserializationException(deserialization_error.message,
                                            deserialization_error.source,
                                            deserialization_error.target)

    @property
    def source(self):
        return self.__source

    @property
    def target(self):
        return self.__target

    @property
    def message(self):
        return self.__message
