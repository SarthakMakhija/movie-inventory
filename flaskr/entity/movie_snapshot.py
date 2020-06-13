from datetime import date

from flaskr.entity import db


class MovieSnapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    director = db.Column(db.String(250))
    release_date = db.Column(db.Date)
    release_year = db.Column(db.Integer)

    def __init__(self, title: str, director: str, release_date: date):
        self.title = title
        self.director = director
        self.release_date = release_date
        self.release_year = self.release_date.year
