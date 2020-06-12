from flask_restful import Api

from flaskr.resource.movie_snapshots import MovieSnapshots


class RestResourceRegistry:
    def __init__(self, api: Api):
        api.add_resource(MovieSnapshots, "/movie-snapshots")
