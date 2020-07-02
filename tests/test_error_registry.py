from http import HTTPStatus
from unittest import TestCase

from flaskr.error_registry import ErrorRegistry
from flaskr.error_response import HTTPErrorResponse


class TestErrorRegistry(TestCase):

    def test_should_register_a_HTTP_status_code_against_an_exception(self):
        ErrorRegistry.register_error(Exception,
                                     HTTPErrorResponse(status_code=HTTPStatus.BAD_REQUEST,
                                                       message=""))

        self.assertEqual(HTTPStatus.BAD_REQUEST, ErrorRegistry.errors["Exception"]["status"])

    def test_should_register_a_error_message_against_an_exception(self):
        ErrorRegistry.register_error(Exception,
                                     HTTPErrorResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                                                       message="Internal Server Error"))

        self.assertEqual("Internal Server Error", ErrorRegistry.errors["Exception"]["message"])
