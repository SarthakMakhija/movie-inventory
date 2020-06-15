def mock_omdb_movie_response(*args, **kargs):
    class MockResponse:
        def __init__(self, payload, status_code):
            self.json_data = payload
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "http://www.omdbapi.com/?t=3 idiots":
        return MockResponse({
            "Title": "3 idiots",
            "Director": "Rajkumar Hirani",
            "Released": "25 Dec 2009",
            "Ratings": [{"Source": "internet", "Value": "9/10"}]},
            200
        )
    elif args[0] == "http://www.omdbapi.com/?t=Jumanji":
        return MockResponse({
            "Title": "Jumanji",
            "Director": "Joe Johnston ",
            "Released": "4 Dec 2019",
            "Ratings": [{"Source": "imdb", "Value": "8/10"}]},
            200
        )
    else:
        return {}
