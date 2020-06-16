from typing import TypeVar, Generic, List, Union

T = TypeVar("T")
E = TypeVar("E")


class Success(Generic[T]):

    def __init__(self, t):
        self.__t = t

    @staticmethod
    def of(t: T):
        return Success(t)

    def t(self) -> T:
        return self.__t


class Failure(Generic[E]):
    def __init__(self, e):
        self.__e = e

    @staticmethod
    def of(e: E):
        return Failure(e)

    def e(self) -> E:
        return self.__e


class Response(Generic[T, E]):

    def __init__(self):
        self.__success: List[Success[T]] = []
        self.__failure: List[Failure[E]] = []

    def add(self, response: Union[Success[T], Failure[E]]):
        if isinstance(response, Success):
            self.__add_success(response)
        else:
            self.__add_failure(response)

    def success_at(self, index) -> Success[T]:
        return self.__success[index]

    def failure_at(self, index) -> Failure[T]:
        return self.__failure[index]

    def success_count(self) -> int:
        return len(self.__success)

    def failure_count(self) -> int:
        return len(self.__failure)

    def all_success_t(self) -> List[T]:
        return [success.t() for success in self.__success]

    def all_failure_t(self) -> List[E]:
        return [failure.e() for failure in self.__failure]

    def __add_success(self, t: T):
        self.__success.append(t)

    def __add_failure(self, e: E):
        self.__failure.append(e)
