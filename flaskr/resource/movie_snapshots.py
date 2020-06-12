from flask_restful import Resource

from flaskr.service.movie_snapshots_service import MovieSnapshotsService


class MovieSnapshots(Resource):

    def __init__(self):
        self.movie_snapshots_service = MovieSnapshotsService()

    def get(self):
        return self.movie_snapshots_service.get_all()
