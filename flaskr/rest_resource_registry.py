from flask_restful import Api

from flaskr.error_registry import ErrorRegistry
from flaskr.resource.movie_snapshots_resource import MovieSnapshotsResource
from flaskr.resource.movie_snapshots_registration_request_resource import  MovieSnapshotsRegistrationRequestResource


class RestResourceRegistry:
    def __init__(self, api: Api):
        api.errors = ErrorRegistry.errors
        api.add_resource(MovieSnapshotsResource, "/movie-snapshots")
        api.add_resource(MovieSnapshotsRegistrationRequestResource, "/movie-snapshots/registration-request")




