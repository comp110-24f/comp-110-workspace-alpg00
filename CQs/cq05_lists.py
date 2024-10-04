"""Mutating functions"""

__author__ = "730758034"

def manual_append(added_list: list[int], n: int) -> None:
    added_list.append(n)

def double(replaced_list: list[int]) -> None:
    i: int = 0
    while i < len(replaced_list):
        replaced_list[i] = replaced_list[i] * 2
        i += 1

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)