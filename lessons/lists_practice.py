"""Basic syntax of lists."""

# Create an empty list
my_numbers: list[float] = [] # literal
my_numbers: list[float] = list() # constructor
# print(my_numbers)

# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)

# String analogy
my_name: str = "" # literal
my_name: str = str() # constructor

# Creating an already populated list
game_points: list[int] = [102, 86, 94]
# print(game_points)

# Modifying a list
game_points[2] = 72

# Subscription Notation/Indexing
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)
# print(len(game_points))
game_points.pop(2)
# print(game_points)

# Lists containing multiple types
int_and_float: list[int | float] = [102, 104.5, 203]
int_and_string: list[int | str] = ["hello", 23, "hi"]
# print(int_and_float)
# print(int_and_string)

# Modifying by index
grocery_list: list[str] = ["banana", "milk", "bread"]
# print(grocery_list)
grocery_list[1] = "banana"
print(grocery_list)

def display(integers: list) -> None:
    index: int = 0
    while index < len(integers):
        print(integers[index])
        index += 1

display(game_points)

def assess(q: int, r: int) -> None:
    s: float = 0.0
    r = r+1
    if q % r == 0:
        s = q / r
    else:
        s = float(q % r)
    s = s + 4.0
    print(s)

assess(2, 1)