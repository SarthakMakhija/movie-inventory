from http import HTTPStatus
from unittest import TestCase

from flaskr.error_response import HTTPErrorResponse


class TestHTTPErrorResponse(TestCase):

    def test_should_return_json_representation_of_http_error_response(self):
        response = HTTPErrorResponse(status_code=HTTPStatus.BAD_REQUEST, message="BAD REQUEST")

        self.assertEqual({
            "status": 400,
            "message": "BAD REQUEST"
        }, response.json())

