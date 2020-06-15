from datetime import date, datetime
from typing import List, Dict, Any

import requests


class OmdbMovieClient:

    def get_movies_for(self, titles: List[str]):
        movies: List[Movie] = []
        for title in titles:
            response = requests.get(f"http://www.omdbapi.com/?t={title}")
            movies.append(Movie(response.json()))

        return movies


class Movie:

    def __init__(self, json: Dict[str, Any]):
        self.__title = json["Title"]
        self.__director = json["Director"]
        self.__released_date = datetime.strptime(json["Released"], '%d %b %Y').date()
        self.__ratings = json["Ratings"]

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director

    @property
    def released_date(self):
        return self.__released_date

    def rating_source_at(self, index: int):
        return self.__ratings[index]["Source"]

    def rating_value_at(self, index: int):
        return self.__ratings[index]["Value"]
