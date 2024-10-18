"""Find and remove max function"""

__author__ = "730772599"


def find_and_remove_max(input: list[int]) -> int:
    """Finds and removes all instances of the largest element in a given list"""

    # handles edge case of an empty inputted list
    if len(input) == 0:
        return -1

    max = input[0]  # sets first element as temporary max value
    for element in input:
        if element > max:
            max = element  # reassigns max variable if larger number is found

    """
    # removes all instances of the max value
    temp_list: list[int] = []
    for element in input:
        if element != max:
            temp_list.append(element)

    input = temp_list  # modifies original list
    """

    # removes all instances of the max value
    idx: int = 0
    while idx < len(input):
        if max == input[idx]:
            input.pop(idx)
        else:
            idx += 1

    return max
