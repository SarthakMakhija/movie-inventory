import json
from typing import Dict

import boto3

from core.config.application_config import ApplicationConfig


class SimpleQueueServiceFixture:

    def __init__(self):
        application_config = ApplicationConfig.instance()
        self.client = boto3.client(service_name="sqs", endpoint_url=application_config.get_or_fail("SQS_ENDPOINT_URL"))
        self.queue_url = application_config.get_or_fail("SQS_QUEUE_NAME")

    def read_message(self) -> Dict:
        response = self.client.receive_message(QueueUrl=self.queue_url)
        return json.loads(json.loads(response['Messages'][0]["Body"])["Message"])

    def delete_all(self):
        self.client.purge_queue(QueueUrl=self.queue_url)
