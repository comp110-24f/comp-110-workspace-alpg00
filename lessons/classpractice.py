import math

class Circle:

    radius: float

    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        circ_area: float = math.pi * self.radius ** 2
        return circ_area
    
my_circ: Circle = Circle(r = 2.0)
print(my_circ.area())