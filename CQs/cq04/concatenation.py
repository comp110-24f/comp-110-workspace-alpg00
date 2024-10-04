"""Concatenation function"""

def concat(msg_one: str, msg_two: str) -> str:
    return msg_one + msg_two

if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
