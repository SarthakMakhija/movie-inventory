from unittest import TestCase
from unittest.mock import patch

from flaskr.event.registered_movie_snapshot_event import RegisteredMovieSnapshotEvent
from flaskr.service.registered_movie_snapshot_event_publisher import RegisteredMovieSnapshotEventPublisher


class RegisteredMovieSnapshotEventPublisherTest(TestCase):

    @patch("flaskr.service.registered_movie_snapshot_event_publisher.AwsSnsClient.publish")
    def test_should_publish_movie_snapshot_registered_event_on_sns(self, sns_client_publish_mock):
        registered_movie_snapshot_event_publisher = RegisteredMovieSnapshotEventPublisher()

        registered_movie_snapshot_event_publisher.publish(RegisteredMovieSnapshotEvent("id_001"))

        sns_client_publish_mock.assert_called_once()

    @patch("flaskr.service.registered_movie_snapshot_event_publisher.AwsSnsClient.publish")
    def test_should_publish_movie_snapshot_registered_event_on_sns_with_snapshot_id(self, sns_client_publish_mock):
        movie_snapshot_registered_event_publisher = RegisteredMovieSnapshotEventPublisher()

        movie_snapshot_registered_event_publisher.publish(RegisteredMovieSnapshotEvent("id_001"))

        sns_client_publish_mock.assert_called_once_with(RegisteredMovieSnapshotEvent("id_001"))
