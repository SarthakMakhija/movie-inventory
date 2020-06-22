import unittest
from typing import List

from tests.fixtures.response_builder import ResponseBuilder


class ResponseTest(unittest.TestCase):

    def test_should_return_success_count_of_1(self):
        response = ResponseBuilder().successful_response_with("Success-as-literal").finish()
        success_count = response.success_count()

        self.assertEqual(1, success_count)

    def test_should_return_success_count_of_0(self):
        response = ResponseBuilder().empty_response().finish()
        success_count = response.success_count()

        self.assertEqual(0, success_count)

    def test_should_return_all_success_items(self):
        response = ResponseBuilder()\
            .successful_response_with("Success-as-literal-1")\
            .successful_response_with("Another-successful-response")\
            .finish()

        success_items: List[str] = response.all_success_t()

        self.assertEqual(["Success-as-literal-1", "Another-successful-response"], success_items)

    def test_should_return_failure_count_of_1(self):
        response = ResponseBuilder().failure_response_with("Failure-as-literal").finish()
        failure_count = response.failure_count()

        self.assertEqual(1, failure_count)

    def test_should_return_failure_count_of_0(self):
        response = ResponseBuilder().empty_response().finish()
        failure_count = response.failure_count()

        self.assertEqual(0, failure_count)

    def test_should_return_all_failed_items(self):
        response = ResponseBuilder() \
            .failure_response_with("Failure-as-literal-1") \
            .failure_response_with("Another-failed-response") \
            .finish()

        failure_items: List[str] = response.all_failure_t()

        self.assertEqual(["Failure-as-literal-1", "Another-failed-response"], failure_items)
