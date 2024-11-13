"""File to define Bear class."""

__author__ = "730772599"


class Bear:
    """Bear class with age and hunger_score attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """New bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Updates age and hunger score of bear after one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increases hunger score of bear if it eats."""
        self.hunger_score += num_fish
