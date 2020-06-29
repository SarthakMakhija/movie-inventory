import json
from typing import Dict
from flask import current_app as app

import boto3


class SimpleNotificationServiceClient:

    def __init__(self):
        self.client = boto3.client(service_name="sns", endpoint_url=app.config.get("SNS_ENDPOINT_URL"))
        self.topic_arn = app.config.get("SNS_TOPIC_NAME")

    def publish(self, event: Dict):
        self.client.publish(TopicArn=self.topic_arn,
                            Message=json.dumps({'default': json.dumps(event)}),
                            MessageStructure='json')
