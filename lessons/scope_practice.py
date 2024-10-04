"""Practice with scopes"""

def remove_chars(msg: str, char: str) -> str:
    """"return a copy of msg with all instances of char removed"""
    copy: str = ""
    index = 0
    while index < len(msg):
        if char != msg[index]:
            copy = copy + msg[index]
        index += 1
    return copy

if __name__ == "__main__":
    word: str = "yoyo"
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))