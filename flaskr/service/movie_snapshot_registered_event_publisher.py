from typing import List

from flaskr.client.aws_sns_client import AwsSnsClient
from flaskr.event.movie_snapshot_registered_event import MovieSnapshotRegisteredEvent
from flaskr.model.registered_snapshot import RegisteredSnapshot


class MovieSnapshotRegisteredEventPublisher:

    def __init__(self):
        self.sns_client = AwsSnsClient()

    def publish_event_for(self, registered_snapshots: List[RegisteredSnapshot]):
        for registered_snapshot in registered_snapshots:
            self.sns_client.publish(MovieSnapshotRegisteredEvent(registered_snapshot.snapshot_id))
