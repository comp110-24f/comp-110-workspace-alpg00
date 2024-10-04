"""Program that allows a user to guess a number and see if they guessed correctly."""

__author__ = "730758034"

def guess_a_number() -> None:
    """Declares a secret number, 7, and asks the user to guess that number."""
    secret: int = 7
    guess: int = int(input("Guess a number: ")) # Have to turn the input value to an int
    print("Your guess was " + str(guess)) # Remember to turn the guess variable to a string
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret)) # Remember to turn the secret variable to a string
    else:
        print("Your guess was too high! The secret number is " + str(secret)) # Again remember secret should become string
    return None

if __name__ == "__main__":
    guess_a_number()
