from datetime import date
from typing import List, Dict

import requests

from flaskr.entity.movie_snapshot import MovieSnapshot, MovieSnapshotRating
from flaskr.model.movie_snapshot_registration_request import MovieSnapshotsRegistrationRequest
from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository


class MovieSnapshotsRegistrationService:

    def __init__(self):
        self.movie_snapshots_repository = MovieSnapshotsRepository()

    def register_snapshots_for(self, a_request: MovieSnapshotsRegistrationRequest) -> Dict[str, List[str]]:
        jsons = []
        for title in a_request.titles:
            r = requests.get(f"http://www.omdbapi.com/?t={title}")
            jsons.append(r.json())

        snapshots = []
        for json in jsons:
            ratings = [MovieSnapshotRating(rating["Value"], rating["Source"]) for rating in json["Ratings"]]
            snapshots.append(MovieSnapshot(json["Title"], json["Director"], date(2005, 12, 25), ratings))

        self.movie_snapshots_repository.save_all(snapshots)
