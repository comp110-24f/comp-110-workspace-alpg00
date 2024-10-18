"""Testing the find_and_remove_max function."""

__author__ = "730758034"

from CQs.cq07.find_max import find_and_remove_max

def test_find_and_remove_max_return_value() -> None:
    nums_list: list[int] = [1, 2, 3, 4]
    assert find_and_remove_max(nums_list) == 4

def test_find_and_remove_max_behavior() -> None:
    nums_list: list[int] = [8, 7, 8, 6]
    find_and_remove_max(nums_list)
    assert nums_list == [7, 6]

def test_find_and_remove_max_edge_case() -> None:
    nums_list: list[int] = []
    assert find_and_remove_max(nums_list) == -1

