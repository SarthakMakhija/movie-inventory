import json

import boto3
from flask import current_app as app
from flaskr.event.domain_event import DomainEvent


class SimpleNotificationServiceClient:

    def __init__(self):
        self.client = boto3.client(service_name="sns", endpoint_url=app.config.get("SNS_ENDPOINT_URL"), region_name="us-east-1")
        self.topic_arn = app.config.get("SNS_TOPIC_NAME")

    def publish(self, event: DomainEvent):
        self.client.publish(TopicArn=self.topic_arn,
                            Message=json.dumps({'default': json.dumps(event.__dict__)}),
                            MessageStructure='json')
