from flask_restful import fields


class MovieSnapshotsView:
    DISPLAYABLE_FIELDS = {
        "title": fields.String,
        "director": fields.String
    }

    def __init__(self, title: str, director: str):
        self.__title = title
        self.__director = director

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director
