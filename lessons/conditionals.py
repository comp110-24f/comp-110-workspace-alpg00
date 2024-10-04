"""practice with conditionals"""

def less_than_10(num: int) -> None:
    """Tell me if num is < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
    print("have a nice day")

less_than_10(num=5)

def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not I should eat based on if I am hungry."""
    if hungry: # conditional/boolean expression
        print("Eat some food silly goose!") # "then" block
    else:
        print("Do your Comp 110 homework instead.") # "else" block
    print("I'm proud of you <3")

should_i_eat(hungry = True)

def check_first_letter(word: str, letter: str) -> str:
    """checks if the first character of word is letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"

print(check_first_letter(word = "hello", letter = "e"))

def get_weather_report() -> str:
    weather = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather

get_weather_report()

age: int = 10
age = 18

print(age)

def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price

def get_ticket_price2() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age > 60:
        price: int = 5
    else:
        price: int = 10
    return price

def get_ticket_price3() -> int:
    age: int = int(input("What is your age?"))
    if (age <= 12) or (age > 60):
        price: int = 5
    else:
        price: int = 10
    return price

def get_ticket_price4() -> int:
    age: int = int(input("What is your age?"))
    if age <= 12:
        price: int = 5
    elif age <= 60:
        price: int = 10
    return price

print(get_ticket_price())
print(get_ticket_price2())
print(get_ticket_price3())
print(get_ticket_price4())
