"""File to define River class."""

__author__ = "730758034"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []

        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """This function removes fish older than 3 and bears older than 5 from the river."""
        new_bear: list[Bear] = []  # create new list for bears
        new_fish: list[Fish] = []  # create new list for fish
        
        for bear in self.bears: 
            if bear.age <= 5:
                new_bear.append(bear)  # for bears 5 or under, add to new list
            
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)  # for fish 3 or under, add to new list
            
        self.bears = new_bear  # set self.bears equal to the new bear list with bears under age of 5
        self.fish = new_fish  # set self.fish equal to the new fish list with fish under the age of 3

        return None

    def bears_eating(self):
        """Method that allows bears to eat fish."""
        bear = Bear()  # create an instance of bear
        
        for bear in self.bears:
            if len(self.fish) >= 5:  # if the length of self.fish is at least 5, call remove_fish with argument 3 and the eat method from the bear class with the argument 3.
                self.remove_fish(3)
                bear.eat(3)
            
        return None
    
    def check_hunger(self):
        """Method that checks the hunger of bears and removes a bear if their hunger score is less than 0."""
        surviving_bears: list[Bear] = []  # create new list of bears to copy over surviving bears

        for bear in self.bears:  # for bears in self.bears, if the hunger score of the bear is 0 or greater, append it to the new list
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)

        self.bears = surviving_bears  # set self.bears equal to the new list consisting of surviving bears

        return None
        
    def repopulate_fish(self):
        """Method that allows fish to reproduce."""
        new_fish_count = (len(self.fish) // 2) * 4  # create a new list of fish and make sure for n fish, there will be (n//2) * 4 new Fish added to fish.

        for _ in range(new_fish_count):
            self.fish.append(Fish())  # append Fish to self.Fish

        return None
    
    def repopulate_bears(self):
        """Method that allows bears to reproduce."""
        new_bears_count = len(self.bears) // 2  # create new list of bears and make sure for n bears, there will be n // 2 new Bears added to bears.

        for _ in range(new_bears_count):
            self.bears.append(Bear())  # append Bear to self.bears
        
        return None
    
    def view_river(self):
        """Skeleton method for output."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Call function one_river_day seven times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        
        return None
    
    def remove_fish(self, amount: int) -> None:
        """This function removes an amount of the frontmost fish from the river."""
        new_fish: list[Fish] = []  # create new list of fish
       
        for _ in range(amount, len(self.fish)):  # loop through the fish greater than index 'amount'
            new_fish.append(self.fish[_])  # add these fish to the new fish list
        self.fish = new_fish  # set self.fish equal to the new fish list
        
        return None