from flask import Flask
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware


class XrayTracingConfigurator:

    def __init__(self, app: Flask):
        self.__app = app

    def configure(self, service_name: str):
        xray_recorder.configure(service=service_name)
        XRayMiddleware(self.__app, xray_recorder)
