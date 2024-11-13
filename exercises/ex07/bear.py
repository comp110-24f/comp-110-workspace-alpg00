"""File to define Bear class."""


class Bear:
    """Bear class."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Initializer."""
        self.age = 0  # initialize to 0
        self.hunger_score = 0  # initialize to 0
        return None
    
    def one_day(self):
        """Method that increases age by 1 and decreases hunger score by 1."""
        self.age += 1  # add one to self.age
        self.hunger_score -= 1  # decrease hunger_score by 1
        return None
    
    def eat(self, num_fish: int):
        """Method that adds num_fish to hunger_score."""
        self.hunger_score += num_fish  # add num_fish to hunger_score
        return None