import logging

from flask import has_request_context, request
from flask.logging import default_handler


class LoggingFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        if has_request_context():
            record.uri = request.uri
        else:
            record.uri = None

        super().format(record)


class LoggingConfiguration:
    @staticmethod
    def configure():
        formatter = LoggingFormatter('[%(asctime)s] %(levelname)s %(module)s: %(message)s for %(uri)s')
        default_handler.setFormatter(formatter)
