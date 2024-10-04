"""Program that helps plan costs and required materials for a tea party."""


__author__ = "730758034"


def main_planner(guests: int) -> None:
    """This function is the entrypoint of the program"""
    # must convert the returns from the functions to strings because each function has a return type that is not a string
    print(
        "A Cozy Tea Party for " 
          + str(
              guests
            )
          + " People!")
    print(
        "Tea Bags: "
        + str(
            tea_bags(people = guests)
        )
    )
    print(
        "Treats: "
        + str(
            treats(people = guests)
        )
    )
    print(
        "Cost: $"
        + str(
            cost(tea_count = tea_bags(people = guests), treat_count = treats(people = guests))
            # tea count is dependent on tea bags, which are dependent on number of people coming
            # same logic for treats
            # this is where the cost function connects to the tea_bags and treats functions
        )
    )


def tea_bags(people: int) -> int:
    """This function returns the number of tea bags based on people attending."""
    return people * 2 # assumes that each person will need 2 bags of tea


def treats(people: int) -> int:
    """This function returns the number of treats."""
    return int(tea_bags(people = people) * 1.5) # tea_bags function is called because it is assumed that for each tea bag someone will need 1.5 treats


def cost(tea_count: int, treat_count: int) -> float:
    """This function computes the cost of tea bags and treats combined."""
    return tea_count * 0.5 + treat_count * 0.75 # multiplies tea count and treat count by the cost for one
    # no need to connect the tea_count and treat_count parameters to the tea_bag and treats functions just yet, that will be done in the main_planner function


if __name__ == "__main__":
    main_planner(guests = int(input("How many guests are attending your party? "))) # line that prompts the user to provide an input
