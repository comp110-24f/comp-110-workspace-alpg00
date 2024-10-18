"""Program containing 3 functions that will be tested later."""

__author__ = "730758034"

def only_evens(input: list[int]) -> list:
    """This function takes a list of integers and only returns the even integers."""
    modified: list[int] = [] # create a new empty list.
    for elem in input: # set up a for loop to iterate through each index.
        if elem % 2 == 0: # if the element at a certain index has no remainder when divided by 2,
            modified.append(elem) # append that element to the new list.
    return modified # return the new list that only contians even integers from the original list.

def sub(inp: list[int], start: int, end: int) -> list:
    """This function generates a list which is a subset of its input list, and starts from the start index and ends at the end index in the parameter."""
    new: list[int] = [] # create a new empty list.
    if len(inp) == 0: # if the input list is just [], return that.
        return inp
    for elem in range(start, end): # this for loop iterates through only the values at the chosen start and end indexes.
        new.append(inp[elem]) # it appends every value between these indexes to the new list.
    return new # finally, the new list is returned.

def add_at_index(input: list[int], element: int, idx: int) -> None:
    """This function mutates the input list by adding an element at a chosen index."""
    if idx < 0 or idx > len(input): # checks if the index is not within the range of the list.
        raise IndexError("Index is out of bounds for the input list") # if it isn't, IndexError is raised.
    input.append(0) # add an element at end of the input list to make space.
    i: int = len(input) - 1 # set an index variable equal to original length of input list.
    # The while loop checks to see if the given index is less that the original length of input list,
    # and while that condition is true it moves every element in front of the idx until the apppended
    # element is at idx.
    while idx < i:
        input[i] = input[i - 1]
        i -= 1
    input[idx] = element # right now the element at idx is 0, so we are setting it to the chosen element.
