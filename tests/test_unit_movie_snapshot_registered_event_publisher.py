from unittest import TestCase
from unittest.mock import patch

from flaskr.event.movie_snapshot_registered_event import MovieSnapshotRegisteredEvent
from flaskr.model.registered_snapshot import RegisteredSnapshot
from flaskr.service.movie_snapshot_registered_event_publisher import MovieSnapshotRegisteredEventPublisher


class MovieSnapshotRegisteredEventPublisherTest(TestCase):

    @patch("flaskr.service.movie_snapshot_registered_event_publisher.SimpleNotificationServiceClient")
    def test_should_publish_movie_snapshot_registered_event_given_a_registered_snapshot(self,
                                                                                        sns_client_mock):
        movie_snapshot_registered_event_publisher = MovieSnapshotRegisteredEventPublisher()

        registered_snapshot = RegisteredSnapshot("id_001", "3 iditions")

        movie_snapshot_registered_event_publisher.publish_event_for([registered_snapshot])

        sns_client_mock.return_value.publish.assert_called()

    @patch("flaskr.service.movie_snapshot_registered_event_publisher.SimpleNotificationServiceClient")
    def test_should_publish_movie_snapshot_registered_event_with_snapshot_id_given_a_registered_snapshot(self,
                                                                                                         sns_client_mock):
        movie_snapshot_registered_event_publisher = MovieSnapshotRegisteredEventPublisher()

        registered_snapshot = RegisteredSnapshot("id_001", "3 iditions")

        movie_snapshot_registered_event_publisher.publish_event_for([registered_snapshot])

        sns_client_mock.return_value.publish.assert_called_with(MovieSnapshotRegisteredEvent("id_001"))

    @patch("flaskr.service.movie_snapshot_registered_event_publisher.SimpleNotificationServiceClient")
    def test_should_publish_movie_snapshot_registered_events_given_multiple_registered_snapshots(self,
                                                                                                 sns_client_mock):
        movie_snapshot_registered_event_publisher = MovieSnapshotRegisteredEventPublisher()

        registered_snapshot_1 = RegisteredSnapshot("id_001", "3 iditions")
        registered_snapshot_2 = RegisteredSnapshot("id_002", "Jumanji")

        movie_snapshot_registered_event_publisher.publish_event_for([
            registered_snapshot_1,
            registered_snapshot_2])

        self.assertEqual(sns_client_mock.return_value.publish.call_args_list[0].args[0].snapshot_id, "id_001")
        self.assertEqual(sns_client_mock.return_value.publish.call_args_list[1].args[0].snapshot_id, "id_002")
