from core.security.http_response_header import HttpResponseHeader


class XssProtectionSecurityHeader:
    name: str = "X-XSS-Protection"
    xss_filtering_enabled_flag_value = "1"

    def __init__(self, block_mode: bool):
        self.__block_mode = block_mode

    @staticmethod
    def make_with(block_mode: bool):
        return XssProtectionSecurityHeader(block_mode)

    @staticmethod
    def in_blocked_mode() -> HttpResponseHeader:
        return XssProtectionSecurityHeader.make_with(block_mode=True).as_http_response_header()

    def as_http_response_header(self):
        if self.__block_mode:
            return HttpResponseHeader(XssProtectionSecurityHeader.name,
                                      f"{XssProtectionSecurityHeader.xss_filtering_enabled_flag_value}; "
                                      f"mode=block")
        else:
            return HttpResponseHeader(XssProtectionSecurityHeader.name,
                                      f"{XssProtectionSecurityHeader.xss_filtering_enabled_flag_value}")
