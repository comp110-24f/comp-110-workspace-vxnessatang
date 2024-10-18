"""Test case module for utils"""

__author__ = "730772599"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_empty_list() -> None:
    """Edge case for empty list"""
    assert only_evens([]) == []


def test_only_evens_odds_only() -> None:
    """Edge case for only odd numbers in original list"""
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_only_evens_use_case() -> None:
    """Use case for checking return value"""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]


def test_only_evens_use_case_2() -> None:
    """Use case for checking return value"""
    assert only_evens([1, 10, 8, 31, 49]) == [10, 8]


def test_only_evens_unmutated() -> None:
    """Use case to check that input is not mutated"""
    x: list[int] = [2, 4, 1, 8, 9]
    only_evens(x)
    assert x == [2, 4, 1, 8, 9]


def test_sub_empty_list() -> None:
    """Edge case for empty list"""
    assert sub([], 0, 0) == []


def test_sub_neg_start() -> None:
    """Edge case for negative start index"""
    assert sub([1, 2, 3, 4, 5], -1, 4) == [1, 2, 3, 4]


def test_sub_invalid_end_index() -> None:
    """Edge case for an end index greater than the length of nums list"""
    assert sub([1, 2, 3, 4, 5], 1, 10) == [2, 3, 4, 5]


def test_sub_use_case() -> None:
    """Use case for checking return value"""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_unmutated() -> None:
    """Use case to check that input is not mutated"""
    x: list[int] = [81, 24, 30, 48, 500]
    sub(x, 2, 4)
    assert x == [81, 24, 30, 48, 500]


def test_add_at_index_raises_indexerror():
    """Edge case for if add_at_index raises an IndexError for an invalid index."""
    x: list[int] = [1, 2, 3, 4, 5]
    with pytest.raises(IndexError):
        add_at_index(x, 6, 100)


def test_add_at_index_element_at_end() -> None:
    """Use case for new element being added to the end"""
    x: list[int] = [0, 1, 2]
    add_at_index(x, 3, 3)
    assert x == [0, 1, 2, 3]


def test_add_at_index_empty_list() -> None:
    """Use case for adding element to empty list"""
    x: list[int] = []
    add_at_index(x, 100, 0)
    assert x == [100]


def test_add_at_index_tens_use_case() -> None:
    """Use case for checking return value"""
    assert add_at_index([10, 30, 40, 50], 20, 1) == None


def test_add_at_index_mutated() -> None:
    """Use case to check that input is mutated"""
    x: list[int] = [1, 2, 3]
    add_at_index(x, 0, 0)
    assert x == [0, 1, 2, 3]
