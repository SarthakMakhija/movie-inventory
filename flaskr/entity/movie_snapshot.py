from datetime import date
from typing import List

from flaskr.entity import db


class MovieSnapshotRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(20))
    source = db.Column(db.String(250))
    movie_snapshot_id = db.Column(db.Integer, db.ForeignKey("movie_snapshot.id"), nullable=False)

    def __init__(self, value: str, source: str):
        self.value = value
        self.source = source


class MovieSnapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    director = db.Column(db.String(250))
    release_date = db.Column(db.Date)
    release_year = db.Column(db.Integer)
    ratings = db.relationship("MovieSnapshotRating", backref="movie_snapshot", lazy=True)

    def __init__(self, title: str, director: str, release_date: date, ratings: List[MovieSnapshotRating] = []):
        self.title = title
        self.director = director
        self.release_date = release_date
        self.release_year = self.release_date.year
        self.ratings = ratings
