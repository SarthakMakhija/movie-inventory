from typing import List

from flaskr.client.simple_notification_service_client import SimpleNotificationServiceClient
from flaskr.event.movie_snapshot_registered_event import MovieSnapshotRegisteredEvent
from flaskr.model.registered_snapshot import RegisteredSnapshot


class MovieSnapshotRegisteredEventPublisher:

    def __init__(self):
        self.sns_client = SimpleNotificationServiceClient()

    def publish_events_for(self, registered_snapshots: List[RegisteredSnapshot]):
        for registered_snapshot in registered_snapshots:
            self.sns_client.publish(MovieSnapshotRegisteredEvent(registered_snapshot.snapshot_id))
