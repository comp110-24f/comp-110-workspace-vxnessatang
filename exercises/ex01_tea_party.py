"""Calculates and displays info to plan a tea party for a number of guests"""

__author__: str = "730772599"


def main_planner(guests: int) -> None:
    """Displays info needed to plan the tea party given the number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculates number of tea bags needed based on the number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculates number of tea bags needed based on the number of guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates total cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    """Runs application and prompts user for number of guests"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
