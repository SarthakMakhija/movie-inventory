from typing import Dict

from tests.configuration.configuration_test import TestConfiguration


def mock_omdb_movie_response(*args, **kargs):
    class MockResponse:
        def __init__(self, payload, status_code):
            self.json_data = payload
            self.status_code = status_code

        def json(self):
            return self.json_data

    mock_response_by_request_url: Dict[str, MockResponse] = {
        f"http://www.omdbapi.com/?t=3 idiots&apikey={TestConfiguration.OMDB_API_KEY}": MockResponse({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]},
            200
        ),
        f"http://www.omdbapi.com/?t=Jumanji&apikey={TestConfiguration.OMDB_API_KEY}": MockResponse({
            "Title": "Jumanji",
            "Director": "Joe Johnston ",
            "Released": "4 Dec 2019",
            "Ratings": [{"Source": "imdb", "Value": "8/10"}]},
            200
        )
    }

    return mock_response_by_request_url[args[0]]
