from __future__ import annotations

import json
import unittest
from datetime import date
from unittest.mock import patch

from tests.application_test import application_test
from tests.fixtures.movie_snapshots_builder import MovieSnapshotsBuilder
from tests.test_client import add_test_client


@application_test()
@add_test_client()
class MovieSnapshotResourceTest(unittest.TestCase):

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_return_Ok_given_a_request_to_get_all_movie_snapshots(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get_all.return_value = []
        response = self.test_client.get("/movie-snapshots")
        self.assertEqual(200, response.status_code)

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_return_no_snapshots_given_no_snapshots_exist(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get_all.return_value = []
        response = self.test_client.get("/movie-snapshots")
        self.assertEqual([], response.json)

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_assert_total_snapshots_to_equal_1(self, movie_snapshots_service):
        movie_snapshots_service.return_value.get_all.return_value = [MovieSnapshotsBuilder.any_snapshot().finish()]
        response = self.test_client.get("/movie-snapshots")
        movie_snapshots = response.json
        self.assertEqual(1, len(movie_snapshots))

    @patch("flaskr.resource.movie_snapshots_resource.MovieSnapshotsService")
    def test_should_assert_all_snapshots(self, movie_snapshots_service):
        movie_snapshot = MovieSnapshotsBuilder.snapshot_title("3 idiots") \
            .directed_by("Rajkumar Hirani") \
            .released_on(date(2009, 12, 25)) \
            .add_rating_with(value="9/10", source="internet") \
            .finish()

        expected_json = '[{"title": "3 idiots", "director": "Rajkumar Hirani", "release_year": 2009, "release_date": ' \
                        '"2009-12-25", "ratings": [{"value": "9/10", "source": "internet"}]}]'

        expected_movie_snapshot_views = json.loads(expected_json)

        movie_snapshots = [movie_snapshot]
        movie_snapshots_service.return_value.get_all.return_value = movie_snapshots

        response = self.test_client.get("/movie-snapshots")
        actual_movie_snapshot_views = response.json
        self.assertEqual(expected_movie_snapshot_views, actual_movie_snapshot_views)
