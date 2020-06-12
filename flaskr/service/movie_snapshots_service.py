from flaskr.repository.movie_snapshots_repository import MovieSnapshotsRepository


class MovieSnapshotsService:

    def __init__(self):
        self.movie_snapshots_repository = MovieSnapshotsRepository()

    def get_all(self):
        return self.movie_snapshots_repository.get_all()


