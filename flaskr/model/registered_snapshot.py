from flaskr.entity.movie_snapshot import MovieSnapshot


class RegisteredSnapshot:

    def __init__(self, snapshot_id: int, snapshot_title: str):
        self.__snapshot_id = snapshot_id
        self.__snapshot_title = snapshot_title

    @staticmethod
    def make_from(movie_snapshot: MovieSnapshot):
        return RegisteredSnapshot(movie_snapshot.id, movie_snapshot.title)

    @property
    def snapshot_id(self):
        return self.__snapshot_id

    @property
    def snapshot_title(self):
        return self.__snapshot_title
