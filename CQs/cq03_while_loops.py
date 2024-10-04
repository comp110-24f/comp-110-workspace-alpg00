"""Program that uses a while loop to iterate over a string"""

__author__ = "730758034"

def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index_tracker: int = 0
    while count < len(phrase):
        if search_char == phrase[count]:
            index_tracker += 1
            count += 1
        else:
            count += 1
    return(index_tracker)
    
