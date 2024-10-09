"""Exercise on lists"""

__author__ = "730758034"

# function that checks to see whether or not every element of the list is equal to an integer
def all(nums: list[int], n: int) -> bool:
    i: int = 0
    if len(nums) == 0:
        return False # return False if the list is empty
    while i < len(nums): # while loop to loop through every element
        if nums[i] == n: # if the integer is equal to the element, add one
            i += 1 
        else:
            return False # if the integer is not equal to the element, return False immediately
    return True # if there was no case where False was returned, return True at the very end

# function that returns the largest number in a list of ints
def max(input: list[int]) -> int:
    if len(input) == 0: # if the length of the input list is 0, a ValueError is returned
        raise ValueError("max() arg is an empty list")
    i: int = 0
    max_number: int = input[i] # set max_number equal to the first element of the list
    while i + 1 < len(input): # use i + 1 to account for how we are comparing each integer to the next one
        if max_number < input[i+1]: # compare the previous element stored in max_number to the next element
            max_number = input[i+1] # if the next element is bigger, set max_number equal to the next element
            i += 1 
        else:
            i += 1 # if the next element is not bigger than the current max_number, keep the current max_number and add one to i
    return max_number 

# checks to see if every element is equal in both of the lists
def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    i: int = 0
    if len(list_one) != len(list_two): # if statement to check if the length of the lists are equal
        return False # if not, then it can't be the case that all elements in each list are equal, so return False
    while i < len(list_one):
        if list_one[i] == list_two[i]: # check if every element of list one is equal to list two
            i += 1
        else:
            return False # if there is an instance where they are not equal return False
    return True # if every element is equal, return True

# function that appends the values of the second list to the end of the first list
def extend(first_list: list[int], second_list: list[int]) -> None:
    i: int = 0
    while i < len(second_list): # while loop to loop through every element in the second list to add it to the first list
        first_list.append(second_list[i])
        i += 1
    print(first_list) # print the newly mutated first list
