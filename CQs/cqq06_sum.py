"""Summing the elements of a list using different loops"""

__author__ = "730758034"

# sum of all elements in a list through while loop
def w_sum(vals: list[float]) -> float:
    i: int = 0
    sum: float = vals[i]
    if len(vals) == 0:
        sum = 0.0
    while i + 1 < len(vals):
        sum += vals[i + 1]
        i += 1
    return sum

# sum of all elements in a list through a for...in loop
def f_sum(nums: list[float]) -> float:
    sum: float = 0.0
    if len(nums) == 0:
        sum = 0.0
    for elem in nums:
        sum += elem
    return sum

# sum of all elements in a list using a for...in range(...) loop
def f_range_sum(items: list[float]) -> float:
    sum: float = 0.0
    if  len(items) == 0:
        sum = 0.0
    for idx in range(0, len(items)):
        sum += items[idx]
    return sum