import json

import boto3
from flask import current_app as app


class SimpleQueueServiceFixture:

    def __init__(self):
        self.client = boto3.client(service_name="sqs", endpoint_url=app.config.get("SQS_ENDPOINT_URL"))
        self.queue_url = app.config.get("SQS_QUEUE_NAME")

    def receive_message(self):
        response = self.client.receive_message(QueueUrl=self.queue_url)
        return json.loads(response['Messages'][0]["Body"])["default"]

    def purge_queue(self):
        self.client.purge_queue(QueueUrl=self.queue_url)
