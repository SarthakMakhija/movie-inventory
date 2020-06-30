from __future__ import annotations

from core.security.http_response_header import HttpResponseHeader
from core.security.x_frame_directive import XFrameDirective


class XFrameSecurityHeader:
    name: str = "X-Frame-Options"
    deny_directive = XFrameDirective.DENY

    def __init__(self, directive: XFrameDirective):
        self.__directive = directive

    @staticmethod
    def make_with(directive) -> XFrameSecurityHeader:
        return XFrameSecurityHeader(directive)

    @staticmethod
    def denied() -> HttpResponseHeader:
        return XFrameSecurityHeader \
            .make_with(directive=XFrameSecurityHeader.deny_directive) \
            .as_http_response_header()

    def as_http_response_header(self) -> HttpResponseHeader:
        return HttpResponseHeader(XFrameSecurityHeader.name, self.__directive.value)


