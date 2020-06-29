from flaskr.service.domain_event_publisher import DomainEvent


class MovieSnapshotRegisteredEvent(DomainEvent):

    def __init__(self, snapshot_id: str):
        self.snapshot_id = snapshot_id
