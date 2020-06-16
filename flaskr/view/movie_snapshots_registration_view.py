from __future__ import annotations

from typing import List

from flask_restful import fields

from flaskr.model.movie_registration_snapshots_response import MovieSnapshotsRegistrationResponse
from flaskr.model.registered_snapshot import RegisteredSnapshot


class MovieSnapshotsRegistrationView:
    DISPLAYABLE_FIELDS = {
        "registered_snapshots": fields.Nested({
            "id": fields.Integer,
            "title": fields.String,
        }),
        "registration_failure_titles": fields.Raw
    }

    def __init__(self,
                 registered_snapshots: List[RegisteredSnapshot],
                 registration_failure_titles: List[str]):
        self.__registered_snapshots = [
            {"id": registered_snapshot.snapshot_id,
             "title": registered_snapshot.snapshot_title
             }
            for registered_snapshot in registered_snapshots
        ]
        self.__registration_failure_titles = registration_failure_titles

    @staticmethod
    def make_from(
            movie_snapshot_registration_response: MovieSnapshotsRegistrationResponse) -> MovieSnapshotsRegistrationView:
        return MovieSnapshotsRegistrationView(movie_snapshot_registration_response.registered_snapshots,
                                              movie_snapshot_registration_response.registration_failure_titles)

    @property
    def registered_snapshots(self):
        return self.__registered_snapshots

    @property
    def registration_failure_titles(self):
        return self.__registration_failure_titles
