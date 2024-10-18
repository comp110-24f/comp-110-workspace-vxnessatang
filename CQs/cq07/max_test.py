"""Unit tests for find_max"""

__author__ = "730772599"

from CQs.cq07.find_max import find_and_remove_max


def test_max_test_expected() -> None:
    """Use case to ensure it returns the expected value"""
    assert find_and_remove_max([1, 10, 4, 8, 5]) == 10


def test_max_test_mutated() -> None:
    """Use case to ensure it mutates the input in the expected way"""
    x: list[int] = [1, 3, 2]
    find_and_remove_max(x)
    assert x == [1, 2]


def test_max_test_empty_list() -> None:
    """Edge case for empty input list"""
    assert find_and_remove_max([]) == -1
