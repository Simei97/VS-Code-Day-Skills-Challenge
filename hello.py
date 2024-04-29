import random

msg = "Roll a dice"

print(msg)

def roll_dice():
    return random.randint(1, 6)

msg = "Roll a dice"
print(msg)

result = roll_dice()
print("The dice rolled:", result)