from typing import List, Dict

import requests

from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest


class MovieSnapshotsRegistrationService:

    def register_snapshots_for(self, a_request: MovieSnapshotsRegistrationRequest) -> Dict[str, List[str]]:
        [requests.get(f"http://www.omdbapi.com/?t={title}") for title in a_request.titles]
        pass
