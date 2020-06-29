from flaskr.event.domain_event import DomainEvent


class AwsSnsClient:

    def publish(self, domain_event: DomainEvent):
        pass
