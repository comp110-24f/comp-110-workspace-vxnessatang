"""More list utility functions"""

__author__ = "730772599"


def only_evens(nums: list[int]) -> list[int]:
    """Adds even numbers to a new list so the list only contains even numbers"""
    new_list: list[int] = []  # initializes empty list for even numbers to be added to
    for i in range(len(nums)):
        if nums[i] % 2 == 0:  # checks if number is even
            new_list.append(nums[i])

    return new_list


def sub(nums: list[int], start: int, end: int) -> list[int]:
    """Creates new list containing a subset of the original list"""

    # handles edge case for empty nums list / invalid index for start or end
    if len(nums) == 0 or start >= len(nums) or end <= 0:
        return []

    # handles edge case for a negative start index
    if start < 0:
        start = 0

    # handles edge case for an end index greater than the length of nums list
    if end > len(nums):
        end = len(nums)  # reassigns end index to the last index

    # defines variables for new list
    subset: list[int] = []
    idx: int = start  # sets index at start index to avoid redundancy

    # loops through and adds nums to new list until the end index but not including it
    while idx < end:
        subset.append(nums[idx])
        idx += 1
    return subset


def add_at_index(nums: list[int], new_element: int, new_idx: int) -> None:
    """Adds element at a particular index in the original list"""

    # throws index error when index is out of range
    if new_idx < 0 or new_idx > len(nums):
        raise IndexError("IndexError: Index is out of bounds for the input list")

    nums.append(0)  # adds extra space for new_element
    idx: int = len(nums) - 1  # sets index to the end of the list
    while idx > new_idx:
        nums[idx] = nums[idx - 1]  # shifts elements to the right by 1
        idx -= 1

    nums[new_idx] = new_element  # inserts new element

    return None
