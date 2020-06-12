from flaskr.flask_application import Application

db = Application.instance().db


class MovieSnapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, title: str, director: str):
        self.__title = title
        self.__director = director

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director
