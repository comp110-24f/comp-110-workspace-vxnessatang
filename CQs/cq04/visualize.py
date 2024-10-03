# did not include package name because cq04.[module] led to a ModuleNotFound error
from concatenation import concat
from coordinates import get_coords

"""Imports functions from other modules and uses them"""

__author__ = "730772599"

# global variables
x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
