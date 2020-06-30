import logging
from typing import List

from flaskr.client.simple_notification_service_client import SimpleNotificationServiceClient
from flaskr.event.movie_snapshot_registered_event import MovieSnapshotRegisteredEvent
from flaskr.model.registered_snapshot import RegisteredSnapshot


class MovieSnapshotRegisteredEventPublisher:

    def __init__(self):
        self.sns_client = SimpleNotificationServiceClient()
        self.logger = logging.getLogger(__name__)

    def publish_events_for(self, registered_snapshots: List[RegisteredSnapshot]) -> bool:
        for registered_snapshot in registered_snapshots:
            self.__publish_event_for(registered_snapshot)
        return True

    def __publish_event_for(self, registered_snapshot):
        try:
            self.sns_client.publish(MovieSnapshotRegisteredEvent(registered_snapshot.snapshot_id))
        except Exception:
            self.logger.exception(f"error publishing MovieSnapshotRegisteredEvent for snapshot_id {registered_snapshot.snapshot_id}")
