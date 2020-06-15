from typing import List


class MovieSnapshotsRegistrationRequest:
    def __init__(self, titles: List[str]):
        self.__titles = titles[:]

    @property
    def titles(self):
        return self.__titles
