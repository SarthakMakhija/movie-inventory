from typing import List

from flask import Response
from core.application.application import Application
from core.security.http_response_header import HttpResponseHeader, HttpResponseHeaders
from core.security.http_security_header_config import StrictTransportSecurityHeaderConfig
from core.security.x_content_type_options_security_header import XContentTypeOptionsSecurityHeader
from core.security.strict_transport_security_header import StrictTransportSecurityHeader
from core.security.x_frame_security_header import XFrameSecurityHeader
from core.security.xss_security_header import XssProtectionSecurityHeader

app = Application.instance().flask_application


@app.after_request
def add_security_headers(response: Response):
    security_headers: List[HttpResponseHeader] = []
    security_headers += [XFrameSecurityHeader.denied(),
                         XContentTypeOptionsSecurityHeader.with_no_sniff(),
                         XssProtectionSecurityHeader.in_blocked_mode(),
                         StrictTransportSecurityHeader.for_subdomains_with(max_age=StrictTransportSecurityHeaderConfig.max_age)]

    return HttpResponseHeaders(security_headers).copy_in(response)


