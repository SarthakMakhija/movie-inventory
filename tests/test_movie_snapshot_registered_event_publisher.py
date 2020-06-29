from unittest import TestCase
from unittest.mock import patch

from flaskr.event.movie_snapshot_registered_event import MovieSnapshotRegisteredEvent
from flaskr.service.movie_snapshot_registered_event_publisher import MovieSnapshotRegisteredEventPublisher


class MovieSnapshotRegisteredEventPublisherTest(TestCase):

    @patch("flaskr.service.movie_snapshot_registered_event_publisher.AwsSnsClient.publish")
    def test_should_publish_movie_snapshot_registered_event_on_sns(self, sns_client_publish_mock):
        movie_snapshot_registered_event_publisher = MovieSnapshotRegisteredEventPublisher()

        movie_snapshot_registered_event_publisher.publish(MovieSnapshotRegisteredEvent("id_001"))

        sns_client_publish_mock.assert_called_once()

    @patch("flaskr.service.movie_snapshot_registered_event_publisher.AwsSnsClient.publish")
    def test_should_publish_movie_snapshot_registered_event_on_sns_with_snapshot_id(self, sns_client_publish_mock):
        movie_snapshot_registered_event_publisher = MovieSnapshotRegisteredEventPublisher()

        movie_snapshot_registered_event_publisher.publish(MovieSnapshotRegisteredEvent("id_001"))

        sns_client_publish_mock.assert_called_once_with(MovieSnapshotRegisteredEvent("id_001"))
