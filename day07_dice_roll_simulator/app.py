import random

print("🎲 Dice Roll Simulator")

while True:
    dice = random.randint(1, 6)
    print(f"You rolled: {dice}")

    choice = input("Roll again? (y/n): ").lower()
    if choice != "y":
        print("Thanks for playing! 👋")
        break