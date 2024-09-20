"""While loop that counts the number of instances the letter appears in the phrase"""

__author__ = "730772599"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts the number of instances the search char appears in the phrase"""
    count: int = 0  # defines counter variable
    idx: int = 0  # defines variable to track the index
    while idx < len(phrase):
        if (
            phrase[idx] == search_char
        ):  # checks if phrase char at that index is the same as the search char
            count += (
                1  # increments counter variable after each instance the chars match
            )
        idx += 1  # increments counter variable after each iteration

    return count


print(num_instances(phrase="HelloHeLloHEllo", search_char="e"))
print(num_instances(phrase="HelloHelloHello", search_char="e"))
print(num_instances(phrase="Happy Tuesday!", search_char="y"))
print(num_instances(phrase="Happy Tuesday!", search_char="z"))
