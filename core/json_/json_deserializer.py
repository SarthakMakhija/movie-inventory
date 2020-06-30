from __future__ import annotations

import jsons
from jsons import DeserializationError

from core.exception.json_deserialization_exception import JsonDeserializationException


class Json:

    def __init__(self, payload: str):
        self.__payload = payload

    @staticmethod
    def of(payload: str) -> Json:
        return Json(payload)

    def deserialize_to(self, target: type) -> type:
        try:
            return jsons.loads(self.__payload, target)
        except DeserializationError as ex:
            raise JsonDeserializationException.make_from(ex)
