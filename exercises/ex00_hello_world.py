"""My first exercise in COMP110!"""

__author__ = "730758034"

def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"

def jersey_num(number: int) -> int:
    return number + 1

def make_jersey(name: str, number: int) -> str:
    print(name + " is number " + str(jersey_num(number = number)))
    return name + ":" + str(number + 1)

print(make_jersey(name = "Lytle", number = 7))