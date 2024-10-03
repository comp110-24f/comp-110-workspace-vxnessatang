"""Concatenates two inputted strings"""

__author__ = "730772599"

# global variables
word1: str = "happy"
word2: str = "tuesday"


def concat(a: str, b: str) -> str:
    """Combines the two inputted strings and returns it"""
    return a + b


if __name__ == "__main__":
    print(concat(a=word1, b=word2))
