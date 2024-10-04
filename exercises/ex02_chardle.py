"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730758034"

def main() -> None:
    contains_char(word = input_word(), letter = input_letter()) 
    # this is function calls the other two functions by setting them equal to the parameters of the contains_char function

def input_word() -> str:
    given_word: str = input("Enter a 5-character word: ")
    if len(given_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit() # exit added so that the program can quit if the word is not 5 characters in length
    return given_word # returns word

def input_letter() -> str:
    letter_guess: str = input("Enter a single character: ")
    if len(letter_guess) != 1:
        print("Error: Character must be a single character.")
        exit() # exit added so that the program can quit if the letter is not 1 character in length
    return letter_guess # returns letter

def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0 # count variable set so that the number of instances of letter in word can be counted
    index: int = 0 # index variable set so that what indexes the letter is found at can be displayed
    while index < len(word):
        if letter == word[index]:
            print(letter + " found at index " + str(index))
            count += 1 # one is added to the count variable so that it can later be displayed for how many times letter came up in word
        index += 1 # one is added to the index variable until index the is equal to the word length, then the program stops
    if count > 1: # this sequence of if statements is to print out how many times letter was found in word. 
        print(str(count) + " instances of " + letter + " found in " + word) # instance if there are multiple instances of letter found in word
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word) # instance if there was one instance of letter found in word
    else:
        print("No instances of " + letter + " found in " + word) # instance if no letter was found in word
