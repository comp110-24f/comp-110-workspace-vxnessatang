"""Testing different functions."""


def get_first(input: list[str]) -> str:
    """Returns the first element in the list."""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Pop the first element off of input list."""
    input.pop(0)
    return None


def get_and_remove_first(input: list[str]) -> str:
    """Pops and returns first element in list."""
    first: str = input[0]
    input.pop(0)
    return first
