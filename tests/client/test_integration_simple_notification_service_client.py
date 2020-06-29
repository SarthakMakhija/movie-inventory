import json
import unittest

from flaskr.client.simple_notification_service_client import SimpleNotificationServiceClient
from tests.application_test import application_test
from tests.fixtures.simple_queue_service_fixture import SimpleQueueServiceFixture


@application_test()
class SimpleNotificationServiceClientIntegrationTest(unittest.TestCase):

    def setUp(self) -> None:
        SimpleQueueServiceFixture().purge_queue()

    def test_should_publish_an_event_to_amazon_simple_notification_service(self):
        simple_notification_service_client = SimpleNotificationServiceClient()

        event = {
            "id": "notification-100"
        }
        simple_notification_service_client.publish(event)

        response_event = SimpleQueueServiceFixture().receive_message()
        self.assertEqual("notification-100", json.loads(response_event)["id"])
