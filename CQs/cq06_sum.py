"""Summing the elements of a list using different loops"""

__author__ = "730772599"


def w_sum(vals: list[float]) -> float:
    """Calculates sum of all elements in list using while loop"""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]  # adds value of each element to sum
        idx += 1  # increments index counter
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculates sum of all elements in list using for i in loop"""
    sum: float = 0.0
    for element in vals:
        sum += element  # adds value of each element to sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculates sum of all elements in list using for i in range loop"""
    sum: float = 0.0
    for i in range(len(vals)):
        sum += vals[i]  # adds value of each element to sum
    return sum
