from flaskr.entity import db


class MovieSnapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    director = db.Column(db.String(250))

    def __init__(self, title: str, director: str):
        self.title = title
        self.director = director
