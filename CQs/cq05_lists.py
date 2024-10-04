"""Mutating functions."""

__author__ = "730772599"

# global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(lst: list[int], num: int) -> None:
    """Appends given number to the end of the given list"""
    lst.append(num)
    return None


def double(lst: list[int]) -> None:
    """Doubles every number in the list"""
    idx = 0
    while idx < len(lst):
        lst[idx] = lst[idx] * 2
        idx += 1
    return None


double(list_2)
print(list_1)
print(list_2)
