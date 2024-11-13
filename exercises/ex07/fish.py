"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Initializer."""
        self.age = 0  # initialize age to 0
        return None
    
    def one_day(self):
        """Method that adds one to fish age."""
        self.age += 1  # add one to age
        return None