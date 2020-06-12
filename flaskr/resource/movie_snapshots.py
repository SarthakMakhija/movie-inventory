from typing import List

from flask_restful import Resource, marshal_with

from flaskr.service.movie_snapshots_service import MovieSnapshotsService
from flaskr.view.movie_snapshots_view import MovieSnapshotsView


class MovieSnapshots(Resource):

    def __init__(self):
        self.movie_snapshots_service = MovieSnapshotsService()

    @marshal_with(fields=MovieSnapshotsView.DISPLAYABLE_FIELDS)
    def get(self):
        return [
            MovieSnapshotsView.make_from(movie_snapshot) for movie_snapshot in self.movie_snapshots_service.get_all()
        ]
