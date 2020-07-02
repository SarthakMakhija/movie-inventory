import json

import boto3

from ipe_core.config.application_configuration_store import ApplicationConfigurationStore
from flaskr.event.domain_event import DomainEvent


class SimpleNotificationServiceClient:

    def __init__(self):
        application_config = ApplicationConfigurationStore.instance()
        self.client = boto3.client(service_name="sns",
                                   endpoint_url=application_config.get_or_fail("SNS_ENDPOINT_URL"),
                                   region_name=application_config.get_or_fail("AWS_REGION")
                                   )
        self.topic_arn = application_config.get_or_fail("SNS_TOPIC_NAME")

    def publish(self, event: DomainEvent):
        self.client.publish(TopicArn=self.topic_arn,
                            Message=json.dumps({'default': json.dumps(event.__dict__)}),
                            MessageStructure='json')
