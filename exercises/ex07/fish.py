"""File to define Fish class."""

__author__ = "730772599"


class Fish:
    """Fish class with age attribute."""

    age: int

    def __init__(self):
        """New fish."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Updates age of fish after one day."""
        self.age += 1
        return None
