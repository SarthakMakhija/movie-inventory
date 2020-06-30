from flaskr.event.domain_event import DomainEvent


class MovieSnapshotRegisteredEvent(DomainEvent):

    def __init__(self, snapshot_id: str):
        self.snapshot_id = snapshot_id
        self.type = "com.mydomain.movie_inventory.movie_snapshot_registered"
