import json
import unittest

from flaskr.client.simple_notification_service_client import SimpleNotificationServiceClient
from flaskr.event.domain_event import DomainEvent
from tests.application_test import application_test
from tests.fixtures.simple_queue_service_fixture import SimpleQueueServiceFixture


class TestDomainEvent(DomainEvent):

    def __init__(self, test_id: str):
        self.test_id = test_id


@application_test()
class SimpleNotificationServiceClientIntegrationTest(unittest.TestCase):

    def setUp(self) -> None:
        SimpleQueueServiceFixture().delete_all()

    def test_should_publish_an_event_to_amazon_simple_notification_service(self):
        simple_notification_service_client = SimpleNotificationServiceClient()

        test_domain_event = TestDomainEvent("event_test_id_001")

        simple_notification_service_client.publish(test_domain_event)

        response_event = SimpleQueueServiceFixture().read_message()

        self.assertEqual("event_test_id_001", response_event["test_id"])
