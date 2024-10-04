__author__ = "730758034"

def mimic(message: str) -> str:
    """This function will take your input and repeat it back to you"""
    return message

def main() -> None:
    print(mimic(message = input("What is your message?")))

if __name__ == "__main__":
    main()
