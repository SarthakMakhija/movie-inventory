import importlib
from typing import Type


from core.config.configuration import Configuration
from core.application.application import Application
from core.tracing.xray_patching_libraries import patch


def load_security_module():
    importlib.import_module("core.security.http_security_response_header_interceptor")


def init_app(config: Type[Configuration]) -> Application:
    application = Application.init_app(config)
    load_security_module()
    patch(config().TRACING_PATCHABLE_LIBRARIES)
    return application
