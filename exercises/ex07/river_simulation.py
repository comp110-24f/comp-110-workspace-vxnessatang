"""Simulates life in the river."""

__author__ = "730772599"

from exercises.ex07.river import River

my_river: River = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()
