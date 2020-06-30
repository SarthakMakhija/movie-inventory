from core.security.http_response_header import HttpResponseHeader


class XContentTypeOptionsSecurityHeader:
    name: str = "X-Content-Type-Options"

    def __init__(self):
        self.content_type_option = "nosniff"

    def __as_http_response_header(self) -> HttpResponseHeader:
        return HttpResponseHeader(XContentTypeOptionsSecurityHeader.name, self.content_type_option)

    @staticmethod
    def with_no_sniff() -> HttpResponseHeader:
        return XContentTypeOptionsSecurityHeader().__as_http_response_header()
