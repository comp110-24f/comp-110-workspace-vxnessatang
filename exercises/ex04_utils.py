"""EX04 - List Utility Functions"""

__author__ = "730772599"


def all(lst: list[int], num: int) -> bool:
    """Checks if all of the numbers in the given list are the same as the given num"""

    # returns False if list is empty
    if len(lst) == 0:
        return False

    # iterates through list to check if each element is the same as the given num
    idx: int = 0
    while idx < len(lst):
        if lst[idx] != num:
            return False
        idx += 1
    return True


def max(lst: list[int]) -> int:
    """Finds the greatest number in the list"""

    # raises value error when given an empty list
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")

    idx: int = 1  # starts at 1 to avoid redundant comparison
    max: int = lst[0]  # stores temp max value to compare as it iterates through list
    while idx < len(lst):
        if (
            lst[idx] > max
        ):  # checks if the number at the current index is larger than max
            max = lst[idx]  # reassigns temp max variable
        idx += 1
    return max


def is_equal(lst: list[int], lst2: list[int]) -> bool:
    """Checks if the two inputted lists have the same elements at the same indices"""

    # returns False if lists are different lengths (elements aren't the same)
    if len(lst) != len(lst2):
        return False

    # checks if lists' elements are equal at every index
    idx: int = 0
    while idx < len(lst):
        if lst[idx] != lst2[idx]:  # compares same index in both lists
            return False
        idx += 1
    return True


def extend(lst: list[int], lst2: list[int]) -> None:
    """Appends elements of the second list to the first list"""
    idx: int = 0

    # iterates through list 2 to append each element to the end of list 1
    while idx < len(lst2):
        lst.append(lst2[idx])
        idx += 1
    return None
