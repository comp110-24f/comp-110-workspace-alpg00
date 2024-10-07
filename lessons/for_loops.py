"""Writing a loop that says Good Boy to each dog in the list"""

pets: list[str] = ["Louie", "Bo", "Bear"]
names: list[str] = ["Alyssa", "Janet", "Vrinda"]

# for loop version
for elem in pets:
    print(f"Good boy, {elem}!")

# while loop version
index: int = 0
while index < len(pets):
    print(f"Good boy, {pets[index]}!")
    index += 1

# for loop version
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")

# while loop version
i: int = 0
while i < len(names):
    print(f"{i}: {names[i]}")
    i += 1
