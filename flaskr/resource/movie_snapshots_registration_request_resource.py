from flask_restful import Resource, reqparse


class MovieSnapshotsRegistrationRequestResource(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("titles", action="append", required=True)
        args = parser.parse_args()

        return "", 201
