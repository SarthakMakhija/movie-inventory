from flask_restful import Api

from flaskr.resource.movie_snapshots_resource import MovieSnapshotsResource


class RestResourceRegistry:
    def __init__(self, api: Api):
        api.add_resource(MovieSnapshotsResource, "/movie-snapshots")
