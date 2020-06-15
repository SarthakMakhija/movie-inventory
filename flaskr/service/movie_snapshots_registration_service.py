from typing import List, Dict

from flaskr.logger_factory import LoggerFactory
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest


class MovieSnapshotsRegistrationService:
    def __init__(self):
        self.logger = LoggerFactory.instance().logger()

    def register_snapshots_for(self, a_request: MovieSnapshotsRegistrationRequest) -> Dict[str, List[str]]:
        pass

