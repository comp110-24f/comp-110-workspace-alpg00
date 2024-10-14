"""Writing three functions"""

# takes a list as input and returns the first element
def get_first(m: list[str]) -> str:
    if len(m) == 0:
        return ""
    return m[0]

# takes a list as input and removes the first element
def remove_first(n: list[str]) -> None:
    n.pop(0)

# takes a list as input and returns + removes first element
def get_and_remove_first(input: list[str]) -> str:
    first_elem: str = input[0]
    input.pop(0)
    return first_elem
