"""File to define River class."""

__author__ = "730772599"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class with day, bears, and fish attributes."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of bears and fishes and removes them if they die of old age."""
        # handles case for no bears or fishes in the river
        if len(self.bears) == 0:
            return None

        if len(self.fish) == 0:
            return None

        new_bears: list[Bear] = []
        new_fish: list[Fish] = []

        for element in self.bears:
            new_bears.append(element)

        for element in self.fish:
            new_fish.append(element)

        # checks bears' ages and removes accordingly
        idx: int = 0
        while idx < len(new_bears):
            if new_bears[idx].age > 5:
                new_bears.pop(idx)
            else:
                idx += 1

        # checks fishes' ages and removes accordingly
        idx: int = 0
        while idx < len(new_fish):
            if new_fish[idx].age > 3:
                new_fish.pop(idx)
            else:
                idx += 1

        # updates lists
        self.bears = new_bears
        self.fish = new_fish

        return None

    def remove_fish(self, amount: int) -> None:
        """Removes fish from river."""
        count: int = 0
        while count < amount:
            self.fish.pop(0)  # removes fish from the beginning of the list - FIFO
            count += 1

    def bears_eating(self):
        """Simulates bear eating fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # removes eaten fish from river
                bear.eat(3)  # increases bear's hunger score
        return None

    def check_hunger(self):
        """Checks hunger of bears and removes them if they die of starvation."""
        # handles case for no bears in the river
        if len(self.bears) == 0:
            return None

        new_bears: list[Bear] = []

        for element in self.bears:
            new_bears.append(element)

        # removes bear from river if they have a negative hunger score
        idx: int = 0
        while idx < len(new_bears):
            if new_bears[idx].hunger_score < 0:
                new_bears.pop(idx)
            else:
                idx += 1

        self.bears = new_bears  # updates bear list

        return None

    def repopulate_fish(self):
        """Reproduction of fish (+4 offspring for each pair)."""
        total_fish: int = len(self.fish)
        while total_fish - 2 >= 0:
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Reproduction of bears (+1 offspring for each pair)."""
        total_bears: int = len(self.bears)
        while total_bears - 2 >= 0:
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        """Creates display of day + current bear and fish population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()
