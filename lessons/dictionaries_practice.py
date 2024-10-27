"""CQ08 Help"""

def find_eligible(names: list[str], ages: list[int]) -> dict[str, int]:
    """Find the names and ages of all people old enough to rent a car!"""
    if len(names) != len(ages):
        raise ValueError("Diff lengths.")
    eligible_ppl: dict[str, int] = {}
    for idx in range(0, len(names)):
        if ages[idx] >= 25:# If >=25, add to dict
            eligible_ppl[names[idx]] = ages[idx]
    return eligible_ppl

names = ["Allan", "Ken", "Barbie"]
ages = [23, 26, 25]
renters: dict[str, int] = find_eligible(names, ages)
print(renters)

# Let's not let Ken rent a car...
if "Ken" in renters:
    renters.pop("Ken")

print(renters)

word: str = "yep"

for x in word:
    print(x)

for x in range(0, len(word)):
    print(word[x])

a: str = "Orange"
b: list[str] = ["Orange", "Wake", "Orange"]

def find(interest: str, counties: list[str]) -> int:
    """docstring"""
    if len(counties) == 0:
        return 0
    count: int = 0
    for x in counties:
        if x == interest:
            count += 1
    return count

print(find(a, b))