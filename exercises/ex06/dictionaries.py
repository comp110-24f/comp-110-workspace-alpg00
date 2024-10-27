"""Dictionary utility functions exercise."""

__author__ = "730758034"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys in a dictionary."""
    invert_input: dict[str, str] = {} # set up an empty dictionary.
    
    for key in input_dict: # loop through every key in the input dictionary.
        value: str = input_dict[key] # set up a variable that is assigned to the value (second key) from the input dictionary.
        if value in invert_input: # checking to see if value is already in the new list.
            raise KeyError(f"Duplicate value found for {value}") # if it is, raise the KeyError.
        invert_input[value] = key # add the value from the input dictionary as the key in the new dictionary, and assign that to the key (effectively swapping the keys).
    
    return invert_input # return the new dictionary with swapped keys.


def favorite_colors(fav_dict: dict[str, str]) -> str:
    """Function that returns the most common favorite color."""
    color_counter: dict[str, int] = {} # set up an empty dictionary.
    count: int = 0 # create a counter variable.
    
    for person in fav_dict: # loop through every person in the dictionary.
        color: str = fav_dict[person] # create a color variable and set it equal to the value of the key (in this case the person's favorite color).
        if color in color_counter: # if the color is already present in the new color_counter dictionary,
            count += 1 # add one to count.
        else: # if not,
            count = 1 # set count = 1.
        color_counter[color] = count # the first key in color_counter is now color, and it is assigned the value count.

    most: str = "" # create a variable that the function can return and will be assigned to the color with the most frequent appearances in color_counter.
    max: int = 0 # create a variable that will keep track of the highest count value in the color_counter dictionary.

    for color in color_counter: # loop through every color in color_counter.
        if color_counter[color] > max: # if the frequency of the color is greater than the max variable,
            most = color # set the most frequent color variable to the name of the color.
            max = color_counter[color] # then, set max equal to the frequency of that color since it beat the max, so we need to update the max.
    
    return most # return the color with the most frequency.


def count(values: list[str]) -> dict[str, int]:
    """Function that returns a dictionary of the values and the number of times those values appeared in the input list."""
    value_count_dict: dict[str, int] = {} # set up an empty dictionary that will take in values in the list and their frequency.
    counter: int = 0 # set up a counter variable to count the frequency of an item in a list.

    for idx in range(0, len(values)): # loop through the input list.
        if values[idx] in value_count_dict: # if the item in the input list is already in the dictionary,
            counter += 1 # add one to the counter variable.
        else:
            counter = 1 # if not, set the counter variable equal to one.
        value_count_dict[values[idx]] = counter # assign the current element in the list to a key in the new dictionary, 
        # and assign that key to the counter variable (which keeps track of the element's frequency in the list).
    
    return value_count_dict # return the dictionary containing the elements in the list and the number of times those elements appeared.


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Function that returns a dictionary consisting of the first letters of each word in the list and a list of the words that start with those letters."""
    alphabet_match: dict[str, list[str]] = {} # set up an empty dictionary to append the keys and values to.
    
    for elem in words: # loop through every element in the input list.
        letter: str = elem[0].lower() # create variable "letter" and assign it to the first letter of the current element.
        if letter not in alphabet_match: # if the first letter is not already in the dictionary,
            alphabet_match[letter] = list() # add the letter as a key and set up an empty list to take in values for that key.
        alphabet_match[letter].append(elem) # append the word that has that first letter to the list that corresponds with the value of the letter key.

    return alphabet_match # return the new dictionary.


def update_attendance(day_att: dict[str, list[str]], day: str, student: str) -> None:
    """Function that updates an attendance dictionary to include the new information that was passed."""
    
    if day in day_att: # check to see if the given day is already in the dictionary.
        day_att[day].append(student) # if it is, just append the given student to the list of values that is already present for that day.
    else: # if the given day is not already in the dictionary,
        day_att[day] = list() # add the given day to the dictionary and assign an empty list to that day.
        day_att[day].append(student) # then, append the student's name to that list.
        
    return None # return nothing because this function only modifies the input dictionary.