"""Testing functions in list_fns."""

from list_fns import get_first, remove_first


def test_get_first() -> None:
    assert get_first(input=["Viktorya", "Samy", "Izzi"]) == "Viktorya"


def test_remove_first() -> None:
    my_TAs: list[str] = ["Viktorya", "Samy", "Benjamin"]
    remove_first(my_TAs)
    assert my_TAs == ["Samy", "Benjamin"]


# run: python -m pytest /workspace/lessons/unit_tests/list_fns_test.py
