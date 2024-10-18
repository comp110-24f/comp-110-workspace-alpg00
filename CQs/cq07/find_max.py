"""Function that finds and removes the max value in a list."""

__author__ = "730758034"

def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    max = input[0]
    for elem in input:
        if elem > max:
            max = elem
    i: int = 0
    while i < len(input):
        if input[i] == max:
            input.pop(i)
            i -= 1
        i += 1
    return max

        