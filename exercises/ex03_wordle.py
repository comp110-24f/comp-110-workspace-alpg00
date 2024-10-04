"""A word guessing game similar to wordle"""

__author__ = "730758034"

def main(main_secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns_taken: int = 1
    guess_input: str = ""
    #while loop implemented to print number of turns taken and call all other functions in the program
    while turns_taken <= 6:
        print(f"=== Turn {turns_taken}/6 ===") # this is to print how many turns have been taken each turn
        guess_input = input_guess(len(main_secret)) # set guess_input equal to the result of input_guess if its parameter was the length of main_secret
        print(emojified(guess_input, main_secret))
        #if statement to check if player won before 6 turns
        if guess_input == main_secret:
            print(f"You won in {turns_taken}/6 turns!") # win message
            return None # return None, program ends
        else:
            turns_taken += 1 # adds one to turns_taken
    print(f"X/6 - Sorry, try again tomorrow!") # if player couldn't win in 6 turns, exit while loop after printing this message
    return None # program ends

def input_guess(secret_word_len: int) -> str:
    """This function prompts the user for an input which is the same length as secret_word_len"""
    enter_word = input(f"Enter a {secret_word_len} character word: ")
    #while loop to check if guess is correct length
    while len(enter_word) != secret_word_len:
        if len(enter_word) != secret_word_len: # if statement to check if the length of the input word is the same as the length of what it is supposed to be
            enter_word = input(f"That wasn't {secret_word_len} chars! Try again: ") # prompts user to enter another word that matches the word length
    return enter_word # returns the word if the user inputted a word with the required amount of characters

def contains_char(secret_word: str, char: str) -> bool:
    """This function searches input_word for an instance of char"""
    assert len(char) == 1 
    i: int = 0
    #while loop to see if letter is in word
    #return true of the letter is contained in the word, and false otherwise
    while i < len(secret_word):
        if secret_word[i] == char: # if statement to check if the character is contained in the word
            return True
        i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """This function shows the user which words they guessed right by returning emojis"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    output: str = ""
    j: int = 0
    # while loop to assign an emoji to each character in the guessed word 
    # depending on whether the character in the guess is in the right place, present, or not present at all
    while j < len(secret):
        if guess[j] == secret[j]: # if indexes have the same character, add a green box emoji to the output
            output += GREEN_BOX
        elif contains_char(secret, guess[j]): # if the character is present in the actual word, add a yellow box to output
            output += YELLOW_BOX
        else: # if the character is not present, add a white box to output
            output += WHITE_BOX
        j += 1
    return output # return the variable output which is now a string containing the colors for each character in the guessed word

if __name__ == "__main__":
	main(main_secret = "codes")