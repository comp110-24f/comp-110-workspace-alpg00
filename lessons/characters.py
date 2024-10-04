"""Practice with while loops"""

#def characters(msg: str) -> None:
    #index: int = 0
    #while index < len(msg):
        #print(msg[index])
        #index += 1


#characters(msg="Howdy")

# def chars(msg: str) -> str:
#     idx: int = 0
#     copy: str = msg
#     while idx < len(msg):
#         print(idx)
#         idx += 1
#     return copy

# a: str = "Hey"
# b: str = "Hi"
# chars(msg=a)

def double(x: int) -> int:
    return x * 2

def double_display(y: int):
    print(y * 2)

double_display(2)
    
if __name__ == "__main__":
    print(double(3))