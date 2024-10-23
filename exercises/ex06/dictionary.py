"""Dictionary Utility Functions"""

__author__ = "730772599"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in list"""
    temp_dict: dict[str, str] = {}  # temporary dictionary to flip keys and values in
    for key in input:
        if input[key] in temp_dict:  # checks for duplicate new keys
            raise KeyError("Error: Duplicate keys found when trying to invert list.")
        temp_dict[input[key]] = key
    return temp_dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns the most popular color based on highest frequency in a list"""
    freq_dict: dict[str, int] = {}

    # sets up color frequency dictionary to reference later
    for element in input:
        if input[element] in freq_dict:
            freq_dict[
                input[element]
            ] += 1  # increments value when another instance is found
        else:
            freq_dict[input[element]] = 1

    max: int = 0  # temp max variable of 0 because it's counting frequency
    color: str = ""  # temp color variable
    for key in freq_dict:
        if freq_dict[key] > max:
            max = freq_dict[key]
            color = key  # stores color associated with new max value
    return color


def count(input: list[str]) -> dict[str, int]:
    """Returns dictionary of the frequency of each value in a list"""
    freq_dict: dict[str, int] = {}
    for element in input:
        if element in freq_dict:
            freq_dict[element] += 1  # increments value when another instance is found
        else:
            freq_dict[element] = 1
    return freq_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns dictionary of letters and lists of words staring with that letter"""
    temp_dict: dict[str, list[str]] = {}
    letter: str = ""
    words: list[str] = []
    for element in input:
        if (
            element[0] not in temp_dict
        ):  # checks that letter doesn't exist in dictionary already
            letter = element[0].lower()
            for element in input:
                if element[0].lower() == letter:
                    words.append(
                        element
                    )  # adds words starting with the letter to a list
            temp_dict[letter] = words
            words = []  # resets words list for each new letter
    return temp_dict


def update_attendance(
    attendance: dict[str, list[str]], weekday: str, student: str
) -> None:
    """Updates attendance dictionary with new info"""
    if weekday not in attendance:
        attendance[weekday] = [student]
    else:
        temp_list: list[str] = attendance[weekday]  # creates temporary list
        if student not in attendance[weekday]:
            temp_list.append(student)  # appends new student to temporary list
            attendance[weekday] = temp_list  # reassigns new value to the key
    return None
