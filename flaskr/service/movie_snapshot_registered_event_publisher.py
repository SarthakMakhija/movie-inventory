from flaskr.client.aws_sns_client import AwsSnsClient
from flaskr.event.movie_snapshot_registered_event import MovieSnapshotRegisteredEvent


class MovieSnapshotRegisteredEventPublisher:

    def __init__(self):
        self.sns_client = AwsSnsClient()

    def publish(self, movie_snapshot_registered_event: MovieSnapshotRegisteredEvent):
        self.sns_client.publish(movie_snapshot_registered_event)
        pass
