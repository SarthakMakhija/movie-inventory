from typing import List

from flaskr.model.registered_snapshot import RegisteredSnapshot


class MovieSnapshotsRegistrationResponse:

    def __init__(self,
                 registered_snapshots: List[RegisteredSnapshot],
                 registration_failure_titles: List[str] = []):
        self.__registered_snapshots = registered_snapshots
        self.__registration_failure_titles = registration_failure_titles

    @property
    def registration_failure_titles(self):
        return self.__registration_failure_titles

    @property
    def registered_snapshot_ids(self):
        return [registered_snapshot.snapshot_id for registered_snapshot in self.__registered_snapshots]

    @property
    def registered_snapshot_titles(self):
        return [registered_snapshot.snapshot_title for registered_snapshot in self.__registered_snapshots]

    @property
    def registered_snapshots(self):
        return self.__registered_snapshots
