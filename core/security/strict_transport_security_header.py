from __future__ import annotations

from core.security.http_response_header import HttpResponseHeader


class StrictTransportSecurityHeader:
    name: str = "Strict-Transport-Security"

    def __init__(self, max_age: int, include_sub_domains):
        self.__max_age = max_age
        self.__include_sub_domains = include_sub_domains

    @staticmethod
    def make_with(max_age: int, include_sub_domains=False) -> StrictTransportSecurityHeader:
        return StrictTransportSecurityHeader(max_age, include_sub_domains)

    @staticmethod
    def for_subdomains_with(max_age: int) -> HttpResponseHeader:
        return StrictTransportSecurityHeader \
            .make_with(max_age=max_age,
                       include_sub_domains=True) \
            .as_http_response_header()

    def as_http_response_header(self) -> HttpResponseHeader:
        if self.__include_sub_domains:
            return HttpResponseHeader(StrictTransportSecurityHeader.name,
                                      f"max-age={self.__max_age} ; "
                                      f"includeSubDomains")
        else:
            return HttpResponseHeader(StrictTransportSecurityHeader.name,
                                      f"max-age={self.__max_age}")
