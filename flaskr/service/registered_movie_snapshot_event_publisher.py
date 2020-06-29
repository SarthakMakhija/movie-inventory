from flaskr.client.aws_sns_client import AwsSnsClient
from flaskr.event.registered_movie_snapshot_event import RegisteredMovieSnapshotEvent


class RegisteredMovieSnapshotEventPublisher:

    def __init__(self):
        self.sns_client = AwsSnsClient()

    def publish(self, movie_snapshot_registered_event: RegisteredMovieSnapshotEvent):
        self.sns_client.publish(movie_snapshot_registered_event)
        pass
