"""Prints combinations of each character in the inputs as coordinate point pairs"""

__author__ = "730772599"


def get_coords(xs: str, ys: str) -> None:
    """Gets combination of characters from two inputted strings and formats them"""

    # index counter variables
    x_idx: int = 0
    y_idx: int = 0

    # loops through each character in ys within each character in xs to print pairs
    while x_idx < len(xs):
        while y_idx < len(ys):
            print(f"({xs[x_idx]}, {ys[y_idx]})")  # prints different combinations
            y_idx += 1
        y_idx = 0  # resets y index counter for the next loop with a new x value
        x_idx += 1
